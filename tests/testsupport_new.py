
"""
@copyright: 2012-2016 Carsten Grohmann (as file __init__.py)
@copyright: 2016 Dietmar Schwertberger

@license: MIT (see LICENSE.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""

import os, sys
sys.path.insert(1, os.path.dirname(sys.path[0]))

import errno, fnmatch, glob, shutil, re
import unittest, difflib, logging, imp

import gettext
t = gettext.translation(domain="wxglade", localedir="locale", fallback=True)
t.install("wxglade")

import common
common.init_paths()

import config
config.testing = True
import wxglade, codegen, compat, log

if compat.PYTHON2:
    from StringIO import StringIO
else:
    from io import StringIO


class WXGladeBaseTest(unittest.TestCase):
    "Provide basic functions for all tests"

    longMessage = True

    caseDirectory = 'casefiles' # Directory with input files and (expected) result files
    outDirectory  = 'generated' # Directory with generated result files

    # Language specific constants for file names: language, file prefix, file extensions
    language_constants = [("python","Py", ".py", ".py"),("perl","Pl", ".pl", ".pm"),
                          ("C++","CPP", ".cpp", ".cpp"),("lisp","Lisp", ".lisp",".lisp"),
                          ("XRC","xrc", ".xrc",".xrc")]

    @classmethod
    def setUpClass(cls):
        "Initialise parts of wxGlade before individual tests starts"
        # set icon path back to the default default
        #config.icons_path = 'icons'

        # initialise wxGlade preferences and set some useful values
        common.init_preferences()
        config.preferences.autosave = False
        config.preferences.write_timestamp = False
        config.preferences.show_progress = False
        config.version = '"faked test version"'

        # make e.g. the preview raise Exceptions
        config.testing = True

        # Determinate case and output directory
        cls.caseDirectory = os.path.join( os.path.dirname(__file__), cls.caseDirectory )
        cls.outDirectory  = os.path.join( os.path.dirname(__file__), cls.outDirectory )
        if not os.path.exists(cls.outDirectory): os.mkdir(cls.outDirectory)

        # disable bug dialogs
        sys._called_from_test = True

    @classmethod
    def tearDownClass(cls):
        "Cleanup after all individual tests are done"
        # de-register own logging
        log.deinit()

    def setUp(self):
        "Initialise"
        codegen.BaseLangCodeWriter._show_warnings = False

    def tearDown(self):
        "Cleanup"
        pass

    def _read_file_lines(self, filename):
        "read a file, split into lines and drop 'generated by ...'"
        with open(filename, "rb") as f:
            ret = f.read()
        ret  = ret.split(  b"\r\n" if b"\r\n" in ret  else b"\n" )
        # drop empty lines and 'generated by...'
        while ret and not ret[-1]:
            del ret[-1]
        for i, line in enumerate(ret[:10]):
            if b'generated by wxGlade' in line:
                del ret[i]
                break
        return ret
    
    def _compare_files(self, expected_filename, generated_filename, check_mtime=False):
        self.assertTrue( os.path.isfile(generated_filename), "File %s was not generated"%generated_filename )
        if check_mtime:
            self.assertGreater( os.stat(generated_filename).st_mtime, os.stat(expected_filename).st_mtime,
                                "File was not overwritten" )
        
        # open files, split into lines and convert to str/unicode
        expected  = self._read_file_lines(expected_filename)
        generated = self._read_file_lines(generated_filename)
        if expected==generated: return False
        expected  = [s.decode('ascii', 'replace') for s in expected]
        generated = [s.decode('ascii', 'replace') for s in generated]
        diff = difflib.unified_diff(expected, generated, fromfile=expected_filename, tofile=generated_filename, lineterm='')
        diff = list(diff)
        print( '\n'.join(diff[:40]) )
        if len(diff)>40: print("...")
        #if compat.PYTHON3:
        self.assertFalse( diff, "Generated file and expected result differs:\n%s" % "\n".join(diff) )
        return True

    def _get_casefile_path(self, filename):
        "return the absolute path of an input file or directory; for .py files, this might include _Phoenix/_Classic"
        basename, extension = os.path.splitext(filename)
        if extension.lower() == ".py":
            # search for version specific files
            if compat.IS_CLASSIC:   fn = "%s_Classic%s"%(basename, extension)
            elif compat.IS_PHOENIX: fn = "%s_Phoenix%s"%(basename, extension)
            fn = os.path.join(self.caseDirectory, fn)
            if os.path.exists(fn): return fn  # this could be a directory as well
        if extension.lower() == ".wxg":
            # search for "_Saved" version
            fn = "%s_Saved%s"%(basename, extension)
            fn = os.path.join(self.caseDirectory, fn)
            if os.path.exists(fn): return fn  # this could be a directory as well
        fn = os.path.join(self.caseDirectory, filename)
        if os.path.exists(fn):
            return fn
        return None

    def _get_outputfile_path(self, filename):
        """return the name for an output file

        filename can be
          - a full path, where only the part relative to caseDirectory will be used
          - an absolute path, where only the leafname will be used
          - a relative path"""
        commonpath = os.path.commonprefix( (self.caseDirectory, filename) )
        if commonpath==self.caseDirectory:
            leaf = filename[len(commonpath)+1:]
        elif os.path.isabs(filename):
            leaf = os.path.basename(filename)
        else:
            leaf = filename
        return os.path.join(self.outDirectory, leaf)


class WXGladeCLITest(WXGladeBaseTest):
    @classmethod
    def setUpClass(cls):
        logging.disable(logging.WARNING)
        wxglade.init_stage1()
        wxglade.init_localization()
        wxglade.init_stage2(False)


import xrc2wxg
import wx
import config, common, compat, main

class WXGladeGUITest(WXGladeBaseTest):

    # as  Python created an own instance for each test, we use class variables for persistent storing 'app' and 'frame':
    app         = None # Reference to a wx.App object.   The object is persistent after the creation in setUp().
    frame       = None # Reference to main.wxGladeFrame. The object is persistent after the creation in setUp().
    nolog       = None # nolog: wxWidgets Null logger to suppress error messages
    orig_stdout = None # original fd for stdout

    def mockMessageBox(self, message, caption, *args, **kwargs):
        "Mock object for wx.MessageBox"
        self._messageBox = [message, caption]

    def _assert_message(self, substring, caption ):
        self.assertTrue( self._messageBox, "No %s message generated"%caption )
        generated_message, generated_caption = self._messageBox
        self.assertTrue( generated_caption==caption, "Expected %s message, got %s"%(caption, generated_caption) )
        fmt='%s message does not match: Expected message containing "%s" \ngot wxMessageBox(message="%s", caption="%s")'
        msg = fmt%(caption, substring, self._messageBox[0], self._messageBox[1] )
        self.assertTrue( substring in generated_message, msg )
        self._messageBox = None

    def _assert_error_message(self, substring ):
        self._assert_message(substring, u"Error")
    def _assert_warning_message(self, substring ):
        self._assert_message(substring, u"Warning")
    def _assert_info_message(self, substring ):
        self._assert_message(substring, u"Information")

    @classmethod
    def setUpClass(cls):
        WXGladeBaseTest.setUpClass()
        xrc2wxg._write_timestamp = False

        # create an simply application
        cls.app = wx.App()
        cls.locale = wx.Locale(wx.LANGUAGE_DEFAULT)
        compat.wx_ArtProviderPush(main.wxGladeArtProvider())
        cls.frame = main.wxGladeFrame()

        # suppress wx error messages
        cls.nolog = wx.LogNull()

        #cls.app.SetAssertMode(0) # avoid triggering of wx assertions; sometimes needed for debugging

        # hide all windows
        #cls.frame.Hide()
        #cls.frame.hide_all()

    @classmethod
    def tearDownClass(cls):
        cls.nolog = None

    def setUp(self):
        # redirect stdout
        self.orig_stdout = sys.stdout
        sys.stdout = StringIO()

        # initialise base class
        WXGladeBaseTest.setUp(self)

        # inject mock object for wxMessageBox
        wx.MessageBox = self.mockMessageBox
        self._messageBox = []

        # show dialog "Code generation completed successfully"
        config.preferences.show_completion = True

    def tearDown(self):
        # restore original stdout
        if self.orig_stdout:
            sys.stdout = self.orig_stdout

        # initialise base class
        WXGladeBaseTest.tearDown(self)

    def _process_wx_events(self):
        "Process wx events, because we don't start the main loop"
        for i in range(3):
            wx.SafeYield()
            self.app.ProcessPendingEvents()

    def load_and_generate(self, basename, excluded=None, included=None, test_GUI=True, preview=True):
        "Load a wxGlade document 'basename' and generate code for all languages except the ones in list 'excluded'"
        if included is None:
            languages = set( [l[0] for l in self.language_constants] + ["wxg"] )
        else:
            languages = set(included)
        if excluded is not None:
            languages -= set(excluded)

        # open file
        infilename = self._get_casefile_path('%s.wxg' % basename)
        common.palette._open_app(infilename, use_progress_dialog=False, add_to_history=False)

        # some shortcuts
        tree = common.app_tree
        app = tree.app

        if test_GUI or preview:
            # expand tree and show edit window
            first_window_node = app.node.children[0]
            first_window = first_window_node.widget
            first_window_item = first_window_node.item
        if test_GUI:
            if first_window_item.IsOk():
                tree.expand()
                self._process_wx_events()
                tree.SelectItem(first_window_item)
                self._process_wx_events()
                tree.show_toplevel(first_window_node)
            self._process_wx_events()
        if preview:
            first_window.properties["preview"]()
            self._process_wx_events()

        if compat.PYTHON2:
            # the languages that failed due to differences to expected files
            diff_fails = []
        else:
            # with Python 3, we use subTests
            subtest = 0

        if "wxg" in languages:
            # save file again and check
            generated_filename = self._get_outputfile_path(infilename)
            compare_filename = self._get_casefile_path(infilename)  # some properties may have changed on loading
            common.palette._save_app(generated_filename)
            if compat.PYTHON2:
                if self._compare_files(infilename, generated_filename):
                    diff_fails.append("wxg")
            else:
                with self.subTest(subtest):
                    self._compare_files(infilename, generated_filename)
                subtest += 1

        # try to generate code with empty output path -> will fail
        app.properties["output_path"].set("")
        app.generate_code()

        # first test should fail because no output file is given
        self._assert_error_message( u'You must specify an output file' )

        # now test full code generation
        for language, dummy, ext, dummy in self.language_constants:
            if not language in languages:
                continue

            if language=="C++" and app.multiple_files:
                app_basename = os.path.splitext(config.default_cpp_app_name)[0]
                app_basename = "%s_%s"%(first_window.klass.split("_")[0], app_basename)
                app.app_filename = app_basename
                expected_filename = self._get_casefile_path( "%s.%s"%(app_basename, app.source_extension) )
                # first_window.klass  # 'Bug179_Frame'
            else:
                expected_filename = self._get_casefile_path( '%s%s' % (basename, ext) )
            if not expected_filename: continue
            generated_filename = self._get_outputfile_path(expected_filename)

            # check for language first
            self.assertTrue( language in common.code_writers, "No codewriter loaded for %s" % language )

            # set absolute "Output path", language and generate code
            if language=="C++" and app.multiple_files:
                app.properties["output_path"].set( os.path.dirname(generated_filename) )
            else:
                app.properties["output_path"].set(generated_filename)
            app.properties["language"].set(language)
            self._process_wx_events()
            app.generate_code()

            self._assert_info_message(u'Code generation completed successfully')

            compare_files = [(expected_filename, generated_filename)]
            if language == 'C++':
                if not app.multiple_files:
                    # compare header file as well
                    expected_filename_h  = '%s.%s' % ( os.path.splitext(expected_filename )[0], app.header_extension )
                    generated_filename_h = '%s.%s' % ( os.path.splitext(generated_filename)[0], app.header_extension )
                    compare_files.append( (expected_filename, generated_filename) )
                else:
                    for toplevel in app.node.children:
                        classname = toplevel.widget.klass
                        # class C++ file
                        expected_filename = self._get_casefile_path( "%s.%s"%(classname, app.source_extension) )
                        if expected_filename:
                            compare_files.append( (expected_filename, self._get_outputfile_path(expected_filename) ) )
                        # class header file
                        expected_filename = self._get_casefile_path( "%s.%s"%(classname, app.header_extension) )
                        if expected_filename:
                            compare_files.append( (expected_filename, self._get_outputfile_path(expected_filename) ) )

            for expected_filename, generated_filename in compare_files:
                if compat.PYTHON2:  # no subtests
                    if self._compare_files(expected_filename, generated_filename): diff_fails.append(language)
                else:
                    with self.subTest(subtest):
                        self._compare_files(expected_filename, generated_filename)
                    subtest += 1
        if compat.PYTHON2:
            self.assertFalse(diff_fails, "Expected and generated files do not match for %s"%",".join(diff_fails))

    def _copy_and_modify(self, source, target, original=None, replacement=None):
        if original is None:
            shutil.copy2( source, target )
            return
        with open(source,"rb") as infile:
            content = infile.read().replace(original, replacement)
        with open(target, "wb") as outfile:
            outfile.write(content)
        shutil.copystat( source, target )

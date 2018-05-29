#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx
import wx.grid

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PyOgg2_MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PyOgg2_MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 500))
        
        # Menu Bar
        self.Mp3_To_Ogg_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_OPEN, _("&Open"), "")
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        wxglade_tmp_menu.Append(wx.ID_EXIT, _("&Quit"), "")
        self.Bind(wx.EVT_MENU, self.OnClose, id=wx.ID_EXIT)
        self.Mp3_To_Ogg_menubar.Append(wxglade_tmp_menu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, _("&About"), _("About dialog"))
        self.Bind(wx.EVT_MENU, self.OnAboutDialog, id=wx.ID_ABOUT)
        self.Mp3_To_Ogg_menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.Mp3_To_Ogg_menubar)
        # Menu Bar end
        self.Mp3_To_Ogg_statusbar = self.CreateStatusBar(2)
        
        # Tool Bar
        self.Mp3_To_Ogg_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.TB_TEXT)
        self.SetToolBar(self.Mp3_To_Ogg_toolbar)
        self.Mp3_To_Ogg_toolbar.AddLabelTool(wx.ID_OPEN, _("&Open"), wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, _("Open a file"), _("Open a MP3 file to convert into OGG format"))
        # Tool Bar end
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_BOTTOM)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
        self.button_3 = wx.Button(self.notebook_1_pane_1, wx.ID_OPEN, "")
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.rbx_sampling_rate = wx.RadioBox(self.notebook_1_pane_2, wx.ID_ANY, _("Sampling Rate"), choices=[_("44 kbit"), _("128 kbit")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.cbx_love = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, _(u"\u2665 Love this song"))
        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_pane_3, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.notebook_1_pane_4 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self._lbl_output_filename = wx.StaticText(self.notebook_1_pane_4, wx.ID_ANY, _("File name:"))
        self.text_ctrl_3 = wx.TextCtrl(self.notebook_1_pane_4, wx.ID_ANY, "")
        self.button_4 = wx.Button(self.notebook_1_pane_4, wx.ID_OPEN, "")
        self.checkbox_1 = wx.CheckBox(self.notebook_1_pane_4, wx.ID_ANY, _("Overwrite existing file"))
        self.notebook_1_pane_5 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_1 = wx.StaticText(self.notebook_1_pane_5, wx.ID_ANY, _("Please check the format of those lines manually:\n\nSingle line without any special characters.\n\na line break between new and line: new\nline\na tab character between new and line: new\tline\ntwo backslash characters: \\\\ \nthree backslash characters: \\\\\\ \na double quote: \"\nan escaped new line sequence: \\n"))
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.button_5 = wx.Button(self, wx.ID_CLOSE, "")
        self.button_2 = wx.Button(self, wx.ID_CANCEL, "", style=wx.BU_TOP)
        self.button_1 = wx.Button(self, wx.ID_OK, "", style=wx.BU_TOP)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_BUTTON, self.startConverting, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PyOgg2_MyFrame.__set_properties
        self.SetTitle(_("mp3 2 ogg"))
        self.Mp3_To_Ogg_statusbar.SetStatusWidths([-2, -1])

        # statusbar fields
        Mp3_To_Ogg_statusbar_fields = [_("Mp3_To_Ogg_statusbar"), ""]
        for i in range(len(Mp3_To_Ogg_statusbar_fields)):
            self.Mp3_To_Ogg_statusbar.SetStatusText(Mp3_To_Ogg_statusbar_fields[i], i)
        self.Mp3_To_Ogg_toolbar.Realize()
        self.text_ctrl_1.SetBackgroundColour(wx.NullColour)
        self.rbx_sampling_rate.SetSelection(0)
        self.cbx_love.SetToolTipString(_(u"Yes!\nWe \u2665 it!"))
        self.cbx_love.SetValue(1)
        self.text_ctrl_3.SetToolTipString(_("File name of the output file\nAn existing file will be overwritten without futher information!"))
        self.checkbox_1.SetToolTipString(_("Overwrite an existing file"))
        self.checkbox_1.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PyOgg2_MyFrame.__do_layout
        sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)
        sizer_2 = wx.FlexGridSizer(1, 3, 0, 0)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        _gszr_pane4 = wx.FlexGridSizer(2, 3, 0, 0)
        _szr_pane3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self.notebook_1_pane_2, wx.ID_ANY, _("Misc")), wx.HORIZONTAL)
        _gszr_pane1 = wx.FlexGridSizer(1, 3, 0, 0)
        _lbl_input_filename = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("File name:"))
        _gszr_pane1.Add(_lbl_input_filename, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        _gszr_pane1.Add(self.text_ctrl_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)
        _gszr_pane1.Add(self.button_3, 0, wx.ALL, 5)
        self.notebook_1_pane_1.SetSizer(_gszr_pane1)
        _gszr_pane1.AddGrowableCol(1)
        sizer_4.Add(self.rbx_sampling_rate, 1, wx.ALL | wx.EXPAND, 5)
        sizer_3.Add(self.cbx_love, 0, wx.ALL | wx.SHAPED, 5)
        sizer_4.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_pane_2.SetSizer(sizer_4)
        _szr_pane3.Add(self.text_ctrl_2, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_pane_3.SetSizer(_szr_pane3)
        _gszr_pane4.Add(self._lbl_output_filename, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        _gszr_pane4.Add(self.text_ctrl_3, 0, wx.ALL | wx.EXPAND, 5)
        _gszr_pane4.Add(self.button_4, 0, wx.ALL, 5)
        _gszr_pane4.Add((20, 20), 0, 0, 0)
        _gszr_pane4.Add(self.checkbox_1, 0, wx.ALL | wx.EXPAND, 5)
        _gszr_pane4.Add((20, 20), 0, 0, 0)
        self.notebook_1_pane_4.SetSizer(_gszr_pane4)
        _gszr_pane4.AddGrowableCol(1)
        sizer_5.Add(self.label_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_pane_5.SetSizer(sizer_5)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Input File"))
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Converting Options"))
        self.notebook_1.AddPage(self.notebook_1_pane_3, _("Converting Progress"))
        self.notebook_1.AddPage(self.notebook_1_pane_4, _("Output File"))
        self.notebook_1.AddPage(self.notebook_1_pane_5, _("Some Text"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.button_5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizer_2.Add(self.button_2, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizer_2.Add(self.button_1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_1)
        sizer_1.SetSizeHints(self)
        sizer_1.AddGrowableRow(0)
        sizer_1.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnOpen(self, event):  # wxGlade: PyOgg2_MyFrame.<event_handler>
        print("Event handler 'OnOpen' not implemented!")
        event.Skip()

    def OnClose(self, event):  # wxGlade: PyOgg2_MyFrame.<event_handler>
        print("Event handler 'OnClose' not implemented!")
        event.Skip()

    def OnAboutDialog(self, event):  # wxGlade: PyOgg2_MyFrame.<event_handler>
        print("Event handler 'OnAboutDialog' not implemented!")
        event.Skip()

    def startConverting(self, event):  # wxGlade: PyOgg2_MyFrame.<event_handler>
        print("Event handler 'startConverting' not implemented!")
        event.Skip()

# end of class PyOgg2_MyFrame

class MyFrameGrid(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameGrid.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((492, 300))
        self.grid = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))
        self.static_line = wx.StaticLine(self, wx.ID_ANY)
        self.button = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrameGrid.__set_properties
        self.SetTitle(_("FrameOggCompressionDetails"))
        self.grid.CreateGrid(8, 3)
        self.button.SetFocus()
        self.button.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrameGrid.__do_layout
        self._szr_frame = wx.BoxSizer(wx.VERTICAL)
        self.grid_sizer = wx.FlexGridSizer(3, 1, 0, 0)
        self.grid_sizer.Add(self.grid, 1, wx.EXPAND, 0)
        self.grid_sizer.Add(self.static_line, 0, wx.ALL | wx.EXPAND, 5)
        self.grid_sizer.Add(self.button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.grid_sizer.AddGrowableRow(0)
        self.grid_sizer.AddGrowableCol(0)
        self._szr_frame.Add(self.grid_sizer, 1, wx.EXPAND, 0)
        self.SetSizer(self._szr_frame)
        self._szr_frame.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class MyFrameGrid

if __name__ == "__main__":
    gettext.install("ComplexExampleApp") # replace with the appropriate catalog name

    ComplexExampleApp = wx.PySimpleApp()
    Mp3_To_Ogg = PyOgg2_MyFrame(None, wx.ID_ANY, "")
    ComplexExampleApp.SetTopWindow(Mp3_To_Ogg)
    Mp3_To_Ogg.Show()
    ComplexExampleApp.MainLoop()

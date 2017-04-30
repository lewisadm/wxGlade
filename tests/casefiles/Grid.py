#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
#
# generated by wxGlade "faked test version"
#

import wx
import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.grid_1 = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.grid.EVT_GRID_CMD_CELL_LEFT_CLICK, self.myEVT_GRID_CELL_LEFT_CLICK, self.grid_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.grid_1.CreateGrid(2, 2)
        self.grid_1.SetGridLineColour(wx.Colour(255, 0, 0))
        self.grid_1.SetLabelBackgroundColour(wx.Colour(216, 191, 216))
        self.grid_1.SetColLabelValue(0, "Column A")
        self.grid_1.SetColLabelValue(1, "Column B")
        self.grid_1.SetBackgroundColour(wx.Colour(0, 255, 255))
        self.grid_1.SetCellValue(0, 0, "1")
        self.grid_1.SetRowLabelValue(0, "Row 1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.grid_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def myEVT_GRID_CELL_LEFT_CLICK(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'myEVT_GRID_CELL_LEFT_CLICK' not implemented!")
        event.Skip()

# end of class MyFrame

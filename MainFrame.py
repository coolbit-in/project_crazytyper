# /usr/bin/env python
# -*- coding=utf-8 -*-
#import wx
from mod_InputField import *
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, 
            parent = None,
            id = -1,
            name = "MainFrame",
            size = (800, 600))

        self.panel = wx.Panel(self)
        self.inputField = InputField(self.panel)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    mainFrame = MainFrame()
    mainFrame.Show()
    app.MainLoop()

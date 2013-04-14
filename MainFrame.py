# /usr/bin/env python
# -*- coding=utf-8 -*-

from mod_InputField import *
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, 
            parent = None,
            id = -1,
            name = "MainFrame",
            pos = (100, 100),
            size = (1024, 700))

        self.panel = wx.Panel(self)
        self.inputField = InputField(self.panel)
        self.defaultButtonSize = (150, 60)
        self.restartButton = wx.Button(parent = self.panel,
            label = "重新开始", pos = (823,620), size = (80, 50))
        self.closeButton = wx.Button(parent = self.panel,
            label = "关闭", pos = (923, 620), size = (80, 50))
        self.historyButton = wx.Button(parent = self.panel,
            label = "历史记录", pos = (200, 620), size = (100, 50))
        self.picButton = wx.Button(parent = self.panel,
            label = "指法图示", pos = (25, 100), size = self.defaultButtonSize)
        self.selectButton = wx.Button(parent = self.panel,
            label = "选择教程", pos = (25, 210), size = self.defaultButtonSize)
        self.customButton = wx.Button(parent = self.panel,
            label = "自定义练习", pos = (25, 320), size = self.defaultButtonSize)
        self.gameButton = wx.Button(parent = self.panel,
            label = "小游戏", pos = (25,430), size = self.defaultButtonSize)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    mainFrame = MainFrame()
    mainFrame.Show()
    app.MainLoop()

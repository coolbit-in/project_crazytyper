# /usr/bin/env python
# -*- coding=utf-8 -*-
from mod_PicFrame import *
from mod_InputField import *
from mod_PlotFrame import *


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,
                          parent=None,
                          id=-1,
                          name="MainFrame",
                          pos=(100, 100),
                          size = (1024, 700))

        self.panel = wx.Panel(self)
        self.inputField = InputField(pare=self.panel)
        self.defaultButtonSize = (150, 60)
        self.restartButton = wx.Button(parent=self.panel,
                                       label="重新开始", pos=(823, 620), size = (80, 50))
        self.closeButton = wx.Button(parent=self.panel,
                                     label="关闭", pos=(923, 620), size = (80, 50))
        self.historyButton = wx.Button(parent=self.panel,
                                       label="历史记录", pos=(200, 620), size = (100, 50))
        self.picButton = wx.Button(parent=self.panel,
                                   label="指法图示", pos=(25, 100), size = self.defaultButtonSize)
        self.selectButton = wx.Button(parent=self.panel,
                                      label="选择教程", pos=(25, 210), size = self.defaultButtonSize)
        self.customButton = wx.Button(parent=self.panel,
                                      label="自定义练习", pos=(25, 320), size = self.defaultButtonSize)
        self.gameButton = wx.Button(parent=self.panel,
                                    label="小游戏", pos=(25, 430), size = self.defaultButtonSize)

        # Bind
        self.Bind(wx.EVT_BUTTON, self.OnRestartButton, self.restartButton)
        self.Bind(wx.EVT_BUTTON, self.OnCloseButton, self.closeButton)
        self.Bind(wx.EVT_BUTTON, self.OnHistoryButton, self.historyButton)
        self.Bind(wx.EVT_BUTTON, self.OnPicButton, self.picButton)
        self.Bind(wx.EVT_BUTTON, self.OnSelectButton, self.selectButton)
        self.Bind(wx.EVT_BUTTON, self.OnCustomButton, self.customButton)
        self.Bind(wx.EVT_BUTTON, self.OnGameButton, self.gameButton)

    # def
    def OnSelectButton(self, event):
        pass

    def OnCloseButton(self, event):
        self.Destroy()

    def OnHistoryButton(self, event):
        self.historyFrame = PlotFrame(self)
        self.historyFrame.Show()
        self.historyFrame.Draw()

    def OnPicButton(self, event):
        self.picFrame = PicFrame(parent=self)
        # self.picFrame.Draw()
        self.picFrame.Show()

    def OnCustomButton(self, event):
        # print "ok"
        fileSelect = wx.FileDialog(parent=None,
                                   message="选择文件", defaultDir=os.getcwd(),
                                   wildcard="txt files (*.txt)|*.txt",
                                   style=wx.OPEN)
        if fileSelect.ShowModal() == wx.ID_OK:
            self.inputField.OpenFile(fileSelect.GetPath())
        fileSelect.Destroy()

    def OnGameButton(self, event):
        pass

    def OnRestartButton(self, event):
        self.inputField.ReInit()
        self.inputField.SetStyle(0, self.inputField.LastPosition,
                                 wx.TextAttr(colText="black", colBack="white"))

if __name__ == "__main__":
    app = wx.PySimpleApp()
    mainFrame = MainFrame()
    mainFrame.Show()
    app.MainLoop()

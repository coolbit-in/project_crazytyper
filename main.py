import wx
class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = -1, name = "MainFrame", size = (800, 600))
        self.panel = wx.Panel(self)
        self.textCtrl = wx.TextCtrl(parent = self,pos = (0, 0), size = (800, 600), style = wx.TE_MULTILINE)
        self.textCtrl.SetEditable(False)
        self.textCtrl.WriteText("youyigeguniangtayoudiandianrenxingnihaiyouyidianxiaozhang")
        self.textCtrl.SetInsertionPoint(0)
        self.yellowTextAttr = wx.TextAttr(colBack = "yellow")
        self.textCtrl.SetStyle(self.textCtrl.GetInsertionPoint(),self.textCtrl.GetInsertionPoint()+1, self.yellowTextAttr)
        self.textCtrl.SetFocus()
        self.textCtrl.Bind(wx.EVT_CHAR, self.OnChar)

    def OnChar(self, event):
        print "hi"
        if event.GetKeyCode() == ord(self.textCtrl.GetString(0, 1)):
            print "yes"
        else:
            print "No"

if __name__ == '__main__':
    app = wx.PySimpleApp()
    mainFrame = MainFrame(parent = None)
    mainFrame.Show()
    app.MainLoop()
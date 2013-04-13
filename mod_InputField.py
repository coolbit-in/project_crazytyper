# -*- coding:utf=8 -*-
import wx
class InputField(wx.TextCtrl):
    def __init__(self, pare):
        wx.TextCtrl.__init__(self,
            parent = pare,
            id = -1,
            name = "InputField",
            size = (600, 400),
            pos = (200, 0),
            style = wx.TE_MULTILINE)

        #属性设置
        self.SetFocus()
        self.SetEditable(False)


        self.defaultFont = wx.Font(pointSize = 18,
            family = wx.FONTFAMILY_MODERN,
            style = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL)

        self.SetDefaultStyle(wx.TextAttr(font = self.defaultFont))
        self.WriteText("↲")
        print ord(↲)
        self.InsertionPoint = 0
        #带色字体设置
        #self.whiteTextAttr = wx.TextAttr(colBack = "white")
        #self.yellowTextAttr = wx.TextAttr(colBack = "yellow")
        #self.greenTextAttr = wx.TextAttr(colBack = "green")
        #self.redTextAttr = wx.TextAttr(colBack = "red")
        self.Bind(wx.EVT_CHAR, self.OnInput)


    def ShiftToRight(self):
        self.InsertionPoint += 1;
        self.SetInsertionPointBackColor("while")

    def ShiftToLeft(self):
        self.InsertionPoint -= 1;
    
    def SetInsertionPointColor(self, color):
        self.SetStyle(self.InsertionPoint,
            self.InsertionPoint + 1,
            wx.TextAttr(colText = color))

    def SetInsertionPointBackColor(self, color):
        self.SetStyle(self.InsertionPoint,
            self.InsertionPoint + 1,
            wx.TextAttr(colBack = color))

    def InputRight(self):
        self.SetInsertionPointColor("green")
        self.ShiftToRight()

    def InputError(self):
        self.SetInsertionPointColor("red")
        self.ShiftToRight()

    def GetInputPointText(self):
        #print self.GetString(self.InsertionPoint,
        #    self.InsertionPoint + 1)
        return self.GetString(self.InsertionPoint,
            self.InsertionPoint + 1)

    def OnInput(self, event):
        if event.GetKeyCode() == ord(self.GetInputPointText()):
        #print self.InsertionPoint
        #print "------------------------------"
        #if event.GetKeyCode() == ord(self.GetString(self.InsertionPoint,
        #   self.InsertionPoint + 1)):
            self.InputRight()
        else:
            self.InputError()




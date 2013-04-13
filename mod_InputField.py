# -*- coding:utf=8 -*-
import wx
import time
from mod_InitFile import *
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


        self.defaultFont = wx.Font(pointSize = 15,
            family = wx.FONTFAMILY_MODERN,
            style = wx.FONTSTYLE_NORMAL,
            weight = wx.FONTWEIGHT_NORMAL)
        self.SetDefaultStyle(wx.TextAttr(font = self.defaultFont))
        #print os.getcwd()
        self.OpenFile(os.getcwd() + "/files/testfile_1.txt");
        #self.WriteText("Announcing Foresight Linux 2.5.3. Foresight is a Linux distribution for your desktop")
        #print ord(↲) #FF5151
        self.InsertionPoint = 0
        self.errorNum = 0
        self.rightNum = 0
        self.isBegin = False
        self.beginTime = 0.0
        self.endTime = 0.0
        #Bind
        self.Bind(wx.EVT_CHAR, self.OnInput)
    
    def OpenFile(self, path):
        file = open(InitFile(path, 40))
        for line in file:
            self.WriteText(line)

    def ShiftToRight(self): #光标右移
        self.InsertionPoint += 1;
        #self.SetInsertionPointBackColor("while")
        if self.InsertionPoint == self.LastPosition:
            self.endTime = time.time()
            self.isBegin = False
            self.ShowResult()

    def ShiftToLeft(self): #光标左移
        self.InsertionPoint -= 1;
    
    def SetInsertionPointColor(self, color): #设置光标位置字体颜色
        self.SetStyle(self.InsertionPoint,
            self.InsertionPoint + 1,
            wx.TextAttr(colText = color))

    def SetInsertionPointBackColor(self, color): #设置光标位置背景颜色
        self.SetStyle(self.InsertionPoint,
            self.InsertionPoint + 1,
            wx.TextAttr(colBack = color))

    def InputRight(self): #输入正确
        self.SetInsertionPointColor("green")
        self.ShiftToRight()
        self.rightNum += 1

    def InputError(self): #输入错误
        self.SetInsertionPointColor("red")
        self.ShiftToRight()
        self.errorNum += 1


    def GetInputPointText(self): #获得光标位字符
        #print self.GetString(self.InsertionPoint,
        #    self.InsertionPoint + 1)
        return self.GetString(self.InsertionPoint,
            self.InsertionPoint + 1)

    def OnInput(self, event): #键盘输入事件处理函数
        if self.isBegin == False:
            self.beginTime = time.time()            
            self.isBegin = True

        if event.GetKeyCode() == ord(self.GetInputPointText()):
            self.InputRight()
        else:
            self.InputError()

    def ShowResult(self):
        resultMessage = "你使用了%d秒，打对%d字母，打错%d字母，平均速度:%d/分钟" % (self.endTime - self.beginTime,
            self.rightNum,
            self.errorNum,
            self.rightNum / (self.endTime - self.beginTime)) 
        resultBox = wx.MessageBox(resultMessage, caption = "成绩", style = wx.OK)




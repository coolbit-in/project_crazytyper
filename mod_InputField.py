# -*- coding:utf=8 -*-
import wx
import time
from mod_InitFile import *


class InputField(wx.TextCtrl):

    def __init__(self, pare):
        wx.TextCtrl.__init__(self,
                             parent=pare,
                             id=-1,
                             name="InputField",
                             size=(809, 600),
                             pos = (200, 0),
                             style = wx.TE_MULTILINE)

        # 属性设置

        self.SetEditable(False)

        self.defaultFont = wx.Font(pointSize=15,
                                   family=wx.FONTFAMILY_MODERN,
                                   style=wx.FONTSTYLE_NORMAL,
                                   weight=wx.FONTWEIGHT_NORMAL)
        self.SetDefaultStyle(wx.TextAttr(font=self.defaultFont))
        # print os.getcwd()
        # self.OpenFile(os.getcwd() + "/files/testfile_1.txt");
        # print ord(↲) #FF5151
        self.ReInit()

        # Bind
        self.Bind(wx.EVT_CHAR, self.OnInput)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnPass)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnPass)

    def ReInit(self):
        self.SetFocus()
        # self.Clear()
        self.InsertionPoint = 0
        self.errorNum = 0
        self.rightNum = 0
        self.isBegin = False
        self.beginTime = 0.0
        self.endTime = 0.0

    def OnPass(self, event):  # 不接受鼠标事件
        pass

    def OpenFile(self, path):  # 打开文件
        self.Clear()
        self.ReInit()
        file = open(InitFile(path))
        for line in file:
            self.WriteText(line)
        self.InsertionPoint = 0

    def ShiftToRight(self):  # 光标右移
        self.InsertionPoint += 1
        # self.SetInsertionPointBackColor("while")
        if self.InsertionPoint == self.LastPosition:
            self.endTime = time.time()
            self.isBegin = False
            self.reportResult()
            # self.ReInit()

    def ShiftToLeft(self):  # 光标左移
        self.InsertionPoint -= 1

    def SetInsertionPointColor(self, coltext, colback):  # 设置光标位置字体颜色
        self.SetStyle(self.InsertionPoint,
                      self.InsertionPoint + 1,
                      wx.TextAttr(colText=coltext, colBack=colback))

    def InputRight(self):  # 输入正确
        self.SetInsertionPointColor("green", "white")
        self.ShiftToRight()
        self.rightNum += 1

    def InputError(self):  # 输入错误
        self.SetInsertionPointColor("red", "#FFB2B2")
        # self.SetInsertionPointBackColor("#FF5151")
        self.ShiftToRight()
        self.errorNum += 1

    def GetInputPointText(self):  # 获得光标位字符
        # print self.GetString(self.InsertionPoint,
        #    self.InsertionPoint + 1)
        return self.GetString(self.InsertionPoint,
                              self.InsertionPoint + 1)

    def OnInput(self, event):  # 键盘输入事件处理函数
        if self.isBegin == False:
            self.beginTime = time.time()
            self.isBegin = True

        if event.GetKeyCode() == ord(self.GetInputPointText()):
            self.InputRight()
        else:
            self.InputError()

    def reportResult(self):
        usedTime = self.endTime - self.beginTime
        rN = self.rightNum
        eN = self.errorNum
        speed = rN / float(usedTime) * 60
        correctRate = rN / float(rN + eN) * 100
        timeLog = open(os.getcwd() + "/logs/time.log", "a")
        speedLog = open(os.getcwd() + "/logs/speed.log", "a")
        rateLog = open(os.getcwd() + "/logs/rate.log", "a")
        # data = str(round(usedTime, 2)), str(round(speed, 2)),
        # str(round(correctRate, 2))

        timeLog.write(str(round(usedTime, 2)) + "\n")
        speedLog.write(str(round(speed, 2)) + "\n")
        rateLog.write(str(round(correctRate, 2)) + "\n")

        timeLog.close()
        speedLog.close()
        rateLog.close()

        self.ShowResult(usedTime, rN, eN, speed, correctRate)

    def ShowResult(self, usedTime, rN, eN, speed, cR):  # 显示单次打字结果
        resultMessage = "你使用了%.1f秒，打对%d字母，打错%d字母，平均速度：%.1f/分钟，正确率：%.1f" % (
            usedTime, rN, eN, speed, cR) + "%"
        resultBox = wx.MessageBox(resultMessage, caption="成绩")
        # print usedTime, rN, eN, speed, cR

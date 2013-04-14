#-*- coding:utf=8 -*-
import wx
import os
import wx.lib.plot as wxPlot
import numpy

class DataObj():
    def __init__(self, path = "", color = "black", name = ""):
        dataFile = open(path, "r")
        data = []
        for line in dataFile: 
        #print dataFile.readline()
            data.append(float(line))
        length = len(data)
        for i in range(1, length+1):
            data.insert(i*2-2, i)
        data = numpy.array(data)
        data.shape = (len(data)/2, 2)
        print data
        self.marker = wxPlot.PolyMarker(data,
            legend = name,
            colour = color,
            marker = "circle",
            size = 1)
        self.line = wxPlot.PolySpline(data,
            colour = "black",)
        #self.graphics = ([self.marker, self.line], )

class PlotFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = -1, title = "历史记录",
            size = (600, 400))
        #self.panel = wx.Panel(self)
        self.plotCanvas = wxPlot.PlotCanvas(self)
        self.speedData = DataObj(path = os.getcwd() + "/logs/speed.log",
            color = "red", name = "速度")
        self.rateData = DataObj(path = os.getcwd() + "/logs/rate.log",
            color = "green", name = "正确率")
        self.graph = wxPlot.PlotGraphics([self.speedData.marker, self.speedData.line, self.rateData.marker, self.rateData.line], "记录", "X", "Y")
        #self.graph = wxPlot.PlotGraphics([self.speedData.marker],"记录", "x", "y")
   
    def Draw(self):
        print "ok"
        self.plotCanvas.Draw(self.graph)

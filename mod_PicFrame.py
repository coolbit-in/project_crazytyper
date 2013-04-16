# -*- coding:utf=8 -*-
import wx
import os


class PicFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='指法图示', size=(1024, 420))
        self.panel = wx.Panel(self)
        img = wx.Image(
            os.getcwd() + '/pictures/dazizhifa.jpg', wx.BITMAP_TYPE_ANY)

        wx.StaticBitmap(self.panel, -1, wx.BitmapFromImage(img))

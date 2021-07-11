global xms, xmx, jar
import wx


class CheckFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button = wx.Button(self, id=1, label = '1') #parent, id(ID_ANY), label, pos, size, style, validator, name
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, id=1) #event, handler, source, id
        sizer.Add(self.button, 0, wx.ALL, 5)
        self.button2 = wx.Button(self, id=2, label = '2')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick2, id=2)
        sizer.Add(self.button2, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def ButtonClick(self, event):
        print('Button 1 clicked')
    
    def ButtonClick2(self, event):
        print('Button 2 clicked')
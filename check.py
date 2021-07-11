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
        self.button3 = wx.Button(self, id=3, label = '3')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick3, id=3)
        sizer.Add(self.button3, 0, wx.ALL, 5)
        self.button4 = wx.Button(self, id=4, label = '4')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick4, id=4)
        self.button5 = wx.Button(self, id=5, label = '5')
        sizer.Add(self.button4, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.ButtonClick5, id=5)
        sizer.Add(self.button5, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def ButtonClick(self, event):
        print('Button 1 clicked')
    
    def ButtonClick2(self, event):
        print('Button 2 clicked')

    def ButtonClick3(self, event):
        print('Button 3 clicked')

    def ButtonClick4(self, event):
        print('Button 4 clicked')

    def ButtonClick5(self, event):
        print('Button 5 clicked')




# only for test, should clear the code below when finished / main page would not work because of this.
def run():
    app = wx.App()
    frame = CheckFrame(None, -1, 'RAM allocation test') # id = -1 to put initial value
    frame.Show()
    app.MainLoop()

run()

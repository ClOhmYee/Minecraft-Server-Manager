global xms, xmx, jar
import wx


class CheckFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self, 'Minimal RAM allocation (xms)') #orient, window, label
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
        sizer.Add(self.button4, 0, wx.ALL, 5)
        self.button5 = wx.Button(self, id=5, label = '5')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick5, id=5)
        sizer.Add(self.button5, 0, wx.ALL, 5)
        self.button6 = wx.Button(self, id=6, label = '6')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick6, id=6)
        sizer.Add(self.button6, 0, wx.ALL, 5)
        self.button7 = wx.Button(self, id=7, label = '7')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick7, id=7)
        sizer.Add(self.button7, 0, wx.ALL, 5)
        self.button8 = wx.Button(self, id=8, label = '8')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick8, id=8)
        sizer.Add(self.button8, 0, wx.ALL, 5)
        self.SetSizer(sizer)
        self.button9 = wx.Button(self, id=9, label = '9')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick9, id=9)
        sizer.Add(self.button9, 0, wx.ALL, 5)


    def ButtonClick(self, event): #1024MB
        print('Button 1 clicked')
        xms = '-Xms1024M'
        print(xms)
    
    def ButtonClick2(self, event): #2048MB
        print('Button 2 clicked')
        xms = '-Xms2048M'
        print(xms)

    def ButtonClick3(self, event): #3072MB
        print('Button 3 clicked')
        xms = '-Xms3072M'
        print(xms)

    def ButtonClick4(self, event): #4096MB
        print('Button 4 clicked')
        xms = '-Xms4096M'
        print(xms)

    def ButtonClick5(self, event): #5120MB
        print('Button 5 clicked')
        xms = '-Xms5120M'
        print(xms)

    def ButtonClick6(self, event): #6144MB
        print('Button 6 clicked')
        xms = '-Xms6144M'
        print(xms)

    def ButtonClick7(self, event): #7168MB
        print('Button 7 clicked')
        xms = '-Xms7168M'
        print(xms)

    def ButtonClick8(self, event): #8192MB
        print('Button 8 clicked')
        xms = '-Xms8192M'
        print(xms)

    def ButtonClick9(self, event): #8192MB
        print('Button 9 clicked')
        xms = 'Detail adjustment here'
        print(xms)



# only for test, should clear the code below when finished / main page would not work because of this.
def run():
    app = wx.App()
    frame = CheckFrame(None, -1, 'RAM allocation test') # id = -1 to put initial value
    frame.Show()
    app.MainLoop()

run()

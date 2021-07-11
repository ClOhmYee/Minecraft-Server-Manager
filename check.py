global xmx, jar
import wx
xmx = '0' #test
jar = '1' #test

class CheckFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self, 'Minimal RAM allocation (xms)') #orient, window, label
        self.button = wx.Button(self, id=1, label = '1024MB') #parent, id(ID_ANY), label, pos, size, style, validator, name
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, id=1) #event, handler, source, id
        sizer.Add(self.button, 0, wx.ALL, 5)
        self.button2 = wx.Button(self, id=2, label = '2048MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick2, id=2)
        sizer.Add(self.button2, 0, wx.ALL, 5)
        self.button3 = wx.Button(self, id=3, label = '3072MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick3, id=3)
        sizer.Add(self.button3, 0, wx.ALL, 5)
        self.button4 = wx.Button(self, id=4, label = '4096MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick4, id=4)
        sizer.Add(self.button4, 0, wx.ALL, 5)
        self.button5 = wx.Button(self, id=5, label = '5120MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick5, id=5)
        sizer.Add(self.button5, 0, wx.ALL, 5)
        self.button6 = wx.Button(self, id=6, label = '6144MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick6, id=6)
        sizer.Add(self.button6, 0, wx.ALL, 5)
        self.button7 = wx.Button(self, id=7, label = '7168MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick7, id=7)
        sizer.Add(self.button7, 0, wx.ALL, 5)
        self.button8 = wx.Button(self, id=8, label = '8192MB')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick8, id=8)
        sizer.Add(self.button8, 0, wx.ALL, 5)
        self.button9 = wx.Button(self, id=9, label = 'DETAIL')
        self.Bind(wx.EVT_BUTTON, self.ButtonClick9, id=9)
        sizer.Add(self.button9, 0, wx.ALL, 5)
        self.button_end = wx.Button(self, id=44, label = '44') #NEED TO MOVE
        self.Bind(wx.EVT_BUTTON, self.ButtonEnd, id=44)
        sizer.Add(self.button_end, 0, wx.ALL, 5)
        self.SetSizer(sizer)


        

    def ButtonClick(self, event): #1024MB
        global xms
        print('Button 1 clicked')
        xms = '-Xms1024M'
        print(xms)
    
    def ButtonClick2(self, event): #2048MB
        global xms
        print('Button 2 clicked')
        xms = '-Xms2048M'
        print(xms)

    def ButtonClick3(self, event): #3072MB
        global xms
        print('Button 3 clicked')
        xms = '-Xms3072M'
        print(xms)

    def ButtonClick4(self, event): #4096MB
        global xms
        print('Button 4 clicked')
        xms = '-Xms4096M'
        print(xms)

    def ButtonClick5(self, event): #5120MB
        global xms
        print('Button 5 clicked')
        xms = '-Xms5120M'
        print(xms)

    def ButtonClick6(self, event): #6144MB
        global xms
        print('Button 6 clicked')
        xms = '-Xms6144M'
        print(xms)

    def ButtonClick7(self, event): #7168MB
        global xms
        print('Button 7 clicked')
        xms = '-Xms7168M'
        print(xms)

    def ButtonClick8(self, event): #8192MB
        global xms
        print('Button 8 clicked')
        xms = '-Xms8192M'
        print(xms)

    def ButtonClick9(self, event): #8192MB
        global xms
        print('Button 9 clicked')
        xms = 'Detail adjustment here'
        print(xms)

    def ButtonEnd(self, event): #Double check exit
        dialog = wx.MessageDialog(self, 'Minimal RAM = {}\nMaximum RAM = {}\nYour server bukkit = {}\nAre you sure you want to save this to the program?'.format(xms,xmx,jar), 'Double check', wx.YES_NO)
        if dialog.ShowModal() == wx.ID_YES:
            print('Save approved')
            quit(0)
        else:
            print('Save denied')
        dialog.Destroy()


# only for test, should clear the code below when finished / main page would not work because of this.
def run():
    app = wx.App()
    frame = CheckFrame(None, -1, 'RAM allocation test') # id = -1 to put initial value
    frame.Show()
    app.MainLoop()

run()

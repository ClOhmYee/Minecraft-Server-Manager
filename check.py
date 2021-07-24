import wx, os
import detail, DataTool # use detail.py, DataTool.py




try: # import xms data
    file_xms = open(DataTool.data_path+'\data_xms.txt','r')
    xms = file_xms.read()
    file_xms.close()
except:
    pass
try: # import xmx data
    file_xmx = open(DataTool.data_path+'\data_xmx.txt','r')
    xmx = file_xmx.read()
    file_xmx.close()
except:
    pass
try: #import jar data
    file_jar = open(DataTool.data_path+'\data_jar.txt','r')
    jar = file_jar.read()
    file_jar.close()
except:
    pass




class CheckFrame(wx.Frame):
    def __init__(self, parent, id, title):
# -----------------------------------xms-----------------------------------
        if not os.path.exists(DataTool.data_path):
            os.makedirs(DataTool.data_path)
        wx.Frame.__init__(self, parent, id, title, size=(740,375))
        self.xms = wx.StaticText(self, label = 'Minimum RAM allocation (xms) (1024MB = 1GB)')
        self.xms.SetPosition((5,10))
        self.button = wx.Button(self, id=1, label = '1024MB', pos =(0,30)) #parent, id(ID_ANY), label, pos, size, style, validator, name
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, id=1) #event, handler, source, id
        self.button2 = wx.Button(self, id=2, label = '2048MB', pos =(80,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick2, id=2)
        self.button3 = wx.Button(self, id=3, label = '3072MB', pos =(160,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick3, id=3)
        self.button4 = wx.Button(self, id=4, label = '4096MB', pos =(240,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick4, id=4)
        self.button5 = wx.Button(self, id=5, label = '5120MB', pos =(320,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick5, id=5)
        self.button6 = wx.Button(self, id=6, label = '6144MB', pos =(400,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick6, id=6)
        self.button7 = wx.Button(self, id=7, label = '7168MB', pos =(480,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick7, id=7)
        self.button8 = wx.Button(self, id=8, label = '8192MB', pos =(560,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick8, id=8)
        self.button9 = wx.Button(self, id=9, label = 'DETAIL', pos =(640,30))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick9, id=9)
        self.button_end = wx.Button(self, id=44, label = 'Done', pos = (640,300))
        self.Bind(wx.EVT_BUTTON, self.ButtonEnd, id=44)




# -----------------------------------xmx-----------------------------------
        self.xmx = wx.StaticText(self, label = 'Maximum RAM allocation (xmx) (1024MB = 1GB)')
        self.xmx.SetPosition((5,70))
        self.button11 = wx.Button(self, id=11, label = '1024MB', pos =(0,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick11, id=11)
        self.button12 = wx.Button(self, id=12, label = '2048MB', pos =(80,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick12, id=12)
        self.button13 = wx.Button(self, id=13, label = '3072MB', pos =(160,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick13, id=13)
        self.button14 = wx.Button(self, id=14, label = '4096MB', pos =(240,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick14, id=14)
        self.button15 = wx.Button(self, id=15, label = '5120MB', pos =(320,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick15, id=15)
        self.button16 = wx.Button(self, id=16, label = '6144MB', pos =(400,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick16, id=16)
        self.button17 = wx.Button(self, id=17, label = '7168MB', pos =(480,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick17, id=17)
        self.button18 = wx.Button(self, id=18, label = '8192MB', pos =(560,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick18, id=18)
        self.button19 = wx.Button(self, id=19, label = 'DETAIL', pos =(640,90))
        self.Bind(wx.EVT_BUTTON, self.ButtonClick19, id=19)

        self.jar = wx.StaticText(self, label = 'Type your bukkit name (Extension : . jar) :')
        self.jar.SetPosition((5,140))
        self.g_jar = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.g_jar.SetPosition((240,140))
        self.button_jar = wx.Button(self, id=20, label = 'Save jar name')
        self.button_jar.SetPosition((360,140))
        self.button_jar.Bind(wx.EVT_BUTTON, self.JarClick)
        self.g_jar.Bind(wx.EVT_TEXT_ENTER, self.JarClick)

        self.notice = wx.StaticText(self, label = 'If you downloaded bukkit with this program, the program would have automatically designated the bukkit.')
        self.notice.SetPosition((5,180))
        self.notice.SetFont(DataTool.notice_font)

    def JarClick(self, event):
        global jar
        if self.g_jar.GetValue() == '':
            dialog = wx.MessageDialog(self, 'Please enter your bukkit name before saving.', 'Error', wx.OK)
            dialog.ShowModal()
            dialog.Destroy()
        else:
            dialog = wx.MessageDialog(self, 'Are you sure your bukkit name is {}.jar? (DONT PUT .JAR WHEN TYPING!)'.format(self.g_jar.GetValue()), 'Warning', wx.YES_NO)
            if dialog.ShowModal() == wx.ID_YES:
                jar = self.g_jar.GetValue()+'.jar'
                DataTool.SaveJar(jar)
                print(jar)
            else:
                pass
            dialog.Destroy()



    def ButtonClick(self, event): #1024MB
        global xms
        print('Button 1 clicked')
        xms = '-Xms1024M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick2(self, event): #2048MB
        global xms
        print('Button 2 clicked')
        xms = '-Xms2048M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick3(self, event): #3072MB
        global xms
        print('Button 3 clicked')
        xms = '-Xms3072M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick4(self, event): #4096MB
        global xms
        print('Button 4 clicked')
        xms = '-Xms4096M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick5(self, event): #5120MB
        global xms
        print('Button 5 clicked')
        xms = '-Xms5120M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick6(self, event): #6144MB
        global xms
        print('Button 6 clicked')
        xms = '-Xms6144M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick7(self, event): #7168MB
        global xms
        print('Button 7 clicked')
        xms = '-Xms7168M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick8(self, event): #8192MB
        global xms
        print('Button 8 clicked')
        xms = '-Xms8192M'
        DataTool.SaveXms(xms)
        print(xms)

    def ButtonClick9(self, event): #8192MB
        global xms
        frame = detail.DetailXmsInfo(self, -1, 'Setting specific minimum RAM allocation')
        frame.SetMaxSize(wx.Size(500,170))
        frame.SetMinSize(wx.Size(500,170))
        frame.Show()
        print('Button 9 clicked')

    def ButtonEnd(self, event): #Double check exit
        try:
            file_xms = open(DataTool.data_path+'\data_xms.txt','r')
            xms = file_xms.read()
            file_xms.close()
            file_xmx = open(DataTool.data_path+'\data_xmx.txt','r')
            xmx = file_xmx.read()
            file_xmx.close()
            file_jar = open(DataTool.data_path+'\data_jar.txt','r')
            jar = file_jar.read()
            file_jar.close()
        except:
            dialog = wx.MessageDialog(self, 'At least one value does not exist. Please click after entering all values.', 'Error', wx.OK)
            dialog.ShowModal()
            dialog.Destroy()
        else:
            self.Close()



    def ButtonClick11(self, event): #1024MB
        global xmx
        print('Button 11 clicked')
        xmx = '-Xmx1024M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick12(self, event): #2048MB
        global xmx
        print('Button 12 clicked')
        xmx = '-Xmx2048M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick13(self, event): #3072MB
        global xmx
        print('Button 13 clicked')
        xmx = '-Xmx3072M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick14(self, event): #4096MB
        global xmx
        print('Button 14 clicked')
        xmx = '-Xmx4096M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick15(self, event): #5120MB
        global xmx
        print('Button 15 clicked')
        xmx = '-Xmx5120M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick16(self, event): #6144MB
        global xmx
        print('Button 16 clicked')
        xmx = '-Xmx6144M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick17(self, event): #7168MB
        global xmx
        print('Button 17 clicked')
        xmx = '-Xmx7168M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick18(self, event): #8192MB
        global xmx
        print('Button 18 clicked')
        xmx = '-Xmx8192M'
        DataTool.SaveXmx(xmx)
        print(xmx)

    def ButtonClick19(self, event): #8192MB
        global xmx
        frame = detail.DetailXmxInfo(self, -1, 'Setting specific maximum RAM allocation')
        frame.SetMaxSize(wx.Size(500,170))
        frame.SetMinSize(wx.Size(500,170))
        frame.Show()
        print('Button 19 clicked')




def RunCheck():
    app = wx.App()
    frame = CheckFrame(None, -1, 'RAM allocation test') # id = -1 to put initial value
    frame.SetMaxSize(wx.Size(740,375))
    frame.SetMinSize(wx.Size(740,375))
    frame.Show()
    app.MainLoop()

# RunCheck()
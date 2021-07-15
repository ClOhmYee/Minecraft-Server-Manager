import os
import wx
import check


global xms, xmx, jar, data_path
xms = 'Unassigned'
xmx = 'Unassigned'
jar = 'Unassigned'

data_path = os.path.dirname(__file__)+'\data'
if (os.path.isdir(data_path) == False): # when there is data
    os.mkdir(data_path)
    print('dir init')

# else: # when there is no data





class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        menu_bar = wx.MenuBar()
        menu = wx.Menu()
        menu_bar.Append(menu, 'Menu')
        menu.Append(101,'Adjust RAM allocation')
        self.Bind(wx.EVT_MENU, self.RAM_allocation, id=101)
        menu.Append(102, 'Quit')
        self.Bind(wx.EVT_MENU, self.Quit, id=102)
        self.SetMenuBar(menu_bar)

        self.pnl = wx.Panel(self)
        self.test1 = wx.Button(self.pnl, id=1111, label = 'status', pos =(650,400), size =(100,70))
        self.Bind(wx.EVT_BUTTON, self.Test1, id=1111)

        self.Centre()
        
    def Test1(self, event):
        self.show_status = wx.StaticText(self, label = 'xms = {}, xmx = {}, jar = {}'.format(self.xms,self.xmx,self.jar))
        self.show_status.SetPosition((450,470))


    def RAM_allocation(self,event):
        print('RAM allocation activated.')
        frame = check.CheckFrame(self, -1, 'Server RAM allocation')
        frame.Show()

    def Quit(self, event):
        dialog = wx.MessageDialog(self, 'Are you sure want to quit?', 'Warning', wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            quit(0)
        else:
            pass
        dialog.Destroy()




class CheckFrame(wx.Frame):
    def __init__(self, parent, id, title):
# -----------------------------------xms-----------------------------------
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        self.t_xms = wx.StaticText(self, label = 'Minimum RAM allocation (xms) (1024MB = 1GB)')
        self.t_xms.SetPosition((5,10))
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
        self.t_xmx = wx.StaticText(self, label = 'Maximum RAM allocation (xmx) (1024MB = 1GB)')
        self.t_xmx.SetPosition((5,70))
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

        self.t_jar = wx.StaticText(self, label = 'Type your bukkit name (Extension : . jar) :')
        self.t_jar.SetPosition((5,140))
        g_jar = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        g_jar.SetPosition((240,140))
        self.button_jar = wx.Button(self, id=20, label = 'Save jar name')
        self.button_jar.SetPosition((360,140))
        self.button_jar.Bind(wx.EVT_BUTTON, self.JarClick)
        g_jar.Bind(wx.EVT_TEXT_ENTER, self.JarClick)

    def JarClick(self, event):
        if self.g_jar.GetValue() == '':
            dialog = wx.MessageDialog(self, 'Please enter your bukkit name before saving.', 'Error', wx.OK)
            dialog.ShowModal()
            dialog.Destroy()
        else:
            write_data = self.g_jar.GetValue()
            dialog = wx.MessageDialog(self, 'Are you sure your bukkit name is {}.jar? (DONT PUT .JAR WHEN TYPING!)'.format(write_data), 'Warning', wx.YES_NO)
            if dialog.ShowModal() == wx.ID_YES:
                print(write_data)
                file_jar = open(data_path+'\jar.txt', 'w+')
                file_jar.write(write_data)
                file_jar.close()
            else:
                pass
            dialog.Destroy()

    def SaveData(self, xms):
        file_xms = open(data_path+'\j_xms.txt','w')
        file_xms.write(self)
        file_xms.close()


    def ButtonClick(self, event): #1024MB
        global xms
        print('Button 1 clicked')
        xms = '-Xms1024M'
        file_xms = open(data_path+'\j_xms.txt','w')
        file_xms.write(xms)
        file_xms.close()
        print(self.xms)

    def ButtonClick2(self, event): #2048MB
        global xms
        print('Button 2 clicked')
        self.xms = '-Xms2048M'
        print(xms)

    def ButtonClick3(self, event): #3072MB
        global xms
        print('Button 3 clicked')
        self.xms = '-Xms3072M'
        print(xms)

    def ButtonClick4(self, event): #4096MB
        global xms
        print('Button 4 clicked')
        self.xms = '-Xms4096M'
        print(xms)

    def ButtonClick5(self, event): #5120MB
        global xms
        print('Button 5 clicked')
        self.xms = '-Xms5120M'
        print(xms)

    def ButtonClick6(self, event): #6144MB
        global xms
        print('Button 6 clicked')
        self.xms = '-Xms6144M'
        print(xms)

    def ButtonClick7(self, event): #7168MB
        global xms
        print('Button 7 clicked')
        self.xms = '-Xms7168M'
        print(xms)

    def ButtonClick8(self, event): #8192MB
        global xms
        print('Button 8 clicked')
        self.xms = '-Xms8192M'
        print(xms)

    def ButtonClick9(self, event): #8192MB
        global xms
        frame = DetailXmsInfo(self, -1, 'Setting specific minimum RAM allocation')
        frame.Show()
        print('Button 9 clicked')

    def ButtonEnd(self, event): #Double check exit
        dialog = wx.MessageDialog(self, 'Minimal RAM = {}\nMaximum RAM = {}\nYour server bukkit = {}\nAre you sure you want to save this to the program?'.format(xms,xmx,jar), 'Warning', wx.YES_NO)
        if dialog.ShowModal() == wx.ID_YES:
            print('Save approved')
            self.Close() #close the RAM allocation page
        else:
            print('Save denied')
        dialog.Destroy()




    def ButtonClick11(self, event): #1024MB
        global xmx
        print('Button 11 clicked')
        self.xmx = '-Xmx1024M'
        print(self.xmx)

    def ButtonClick12(self, event): #2048MB
        global xmx
        print('Button 12 clicked')
        self.xmx = '-Xmx2048M'
        print(xmx)

    def ButtonClick13(self, event): #3072MB
        global xmx
        print('Button 13 clicked')
        self.xmx = '-Xmx3072M'
        print(xmx)

    def ButtonClick14(self, event): #4096MB
        global xmx
        print('Button 14 clicked')
        self.xmx = '-Xmx4096M'
        print(xmx)

    def ButtonClick15(self, event): #5120MB
        global xmx
        print('Button 15 clicked')
        self.xmx = '-Xmx5120M'
        print(xmx)

    def ButtonClick16(self, event): #6144MB
        global xmx
        print('Button 16 clicked')
        self.xmx = '-Xmx6144M'
        print(xmx)

    def ButtonClick17(self, event): #7168MB
        global xmx
        print('Button 17 clicked')
        self.xmx = '-Xmx7168M'
        print(xmx)

    def ButtonClick18(self, event): #8192MB
        global xmx
        print('Button 18 clicked')
        self.xmx = '-Xmx8192M'
        print(xmx)

    def ButtonClick19(self, event): #8192MB
        global xmx
        frame = DetailXmxInfo(self, -1, 'Setting specific maximum RAM allocation')
        frame.Show()
        print('Button 19 clicked')



# -----------------------------------xms-----------------------------------
class DetailXmsInfo(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,170))

        self.panel = wx.Panel(self)
        self.t_xms = wx.StaticText(self.panel, label = "Please enter the minimum RAM allocation you want (unit : MB) :")
        self.t_xms.SetPosition((10,50))
        self.g_xms = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        self.g_xms.SetPosition((365,50))

        self.button = wx.Button(self.panel, label = "Done")
        self.button.SetPosition((400,100))
        self.button.Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.g_xms.Bind(wx.EVT_TEXT_ENTER, self.ButtonClick)

    
    def ButtonClick(self,event):
        xms_value = self.g_xms.GetValue()
        dialog = wx.MessageDialog(self, 'Are you sure want to allocate your server minimum RAM : {}MB?'.format(xms_value), 'Warning', wx.YES_NO)
        if dialog.ShowModal() == wx.ID_YES:
            global xms
            self.xms = '-Xms'+str(xms_value)+'M'
            print(xms)
            self.Close() # close the detail page
        else:
            pass
        dialog.Destroy()




# -----------------------------------xmx-----------------------------------
class DetailXmxInfo(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,170))

        self.panel = wx.Panel(self)
        self.t_xmx = wx.StaticText(self.panel, label = "Please enter the maximum RAM allocation you want (unit : MB) :")
        self.t_xmx.SetPosition((10,50))
        g_xmx = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        g_xmx.SetPosition((365,50))

        self.button = wx.Button(self.panel, label = "Done")
        self.button.SetPosition((400,100))
        self.button.Bind(wx.EVT_BUTTON, self.ButtonClick)
        g_xmx.Bind(wx.EVT_TEXT_ENTER, self.ButtonClick)

    
    def ButtonClick(self,event):
        xmx_value = self.g_xmx.GetValue()
        print(xmx_value)
        dialog = wx.MessageDialog(self, 'Are you sure want to allocate your server maximum RAM : {}MB?'.format(xmx_value), 'Warning', wx.YES_NO)
        if dialog.ShowModal() == wx.ID_YES:
            write_xmx = '-Xmx'+str(xmx_value)+'M'
            print(write_xmx)
            xmx_path = data_path+'/xmx.txt'
            print(xmx_path)
            file_xmx = open(xmx_path, 'w')
            file_xmx.write(write_xmx)
            file_xmx.close()
            self.Close() # close the detail page
        else:
            pass
        dialog.Destroy()







def run():
    app = wx.App()
    frame = MainFrame(None, -1, 'Minecraft Server Manager') # id = -1 to put initial value
    frame.Show()
    app.MainLoop()

run()



# number = input('Enter : ')

# if number == '1':
#     boot_path = os.getcwd() + '/start_server.py'
#     exec(open(boot_path).read())
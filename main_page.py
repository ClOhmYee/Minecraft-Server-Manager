import wx, os, shutil
import check, DataTool, start_server, activate_eula, install  # use detail.py, DataTool.py, start_server.py, activate_eula.py, install.py

global xms, xmx, jar

os.chdir(DataTool.base_path)

try: # import xms data
    file_xms = open(DataTool.data_path+'\data_xms.txt','r')
    xms = file_xms.read()
    file_xms.close()
except:
    xms = 'Unassigned'
try: # import xmx data
    file_xmx = open(DataTool.data_path+'\data_xmx.txt','r')
    xmx = file_xmx.read()
    file_xmx.close()
except:
    xmx = 'Unassigned'
try: #import jar data
    file_jar = open(DataTool.data_path+'\data_jar.txt','r')
    jar = file_jar.read()
    file_jar.close()
except:
    jar = 'Unassigned'



class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        menu_bar = wx.MenuBar()
        menu = wx.Menu()
        menu_bar.Append(menu, 'Menu')
        menu.Append(101, 'Settings')
        self.Bind(wx.EVT_MENU, self.Settings, id=101)
        menu.Append(102, 'Quit')
        self.Bind(wx.EVT_MENU, self.Quit, id=102)
        
        menu2 = wx.Menu()
        menu_bar.Append(menu2, 'Open')
        menu2.Append(103, 'Server Properties')
        self.Bind(wx.EVT_MENU, self.OpenProperties, id=103)
        menu2.Append(104, 'Op List')
        self.Bind(wx.EVT_MENU, self.OpenOp, id=104)
        menu2.Append(105, 'Ban-player List')
        self.Bind(wx.EVT_MENU, self.OpenBan, id=105)
        menu2.Append(106, 'Ban-ip List')
        self.Bind(wx.EVT_MENU, self.OpenBanIP, id=106)
        menu2.Append(107, 'Whitelist')
        self.Bind(wx.EVT_MENU, self.OpenWhiteList, id=107)
        menu2.Append(108, 'Bukkit Configuration')
        self.Bind(wx.EVT_MENU, self.OpenBukkit, id=108)
        menu2.Append(109, 'Command Configuration')
        self.Bind(wx.EVT_MENU, self.OpenCommand, id=109)
        menu2.Append(110, 'Spigot Configuration')
        self.Bind(wx.EVT_MENU, self.OpenSpigot, id=110)
        menu2.Append(111, 'Help')
        self.Bind(wx.EVT_MENU, self.OpenHelp, id=111)

        menu3 = wx.Menu()
        menu_bar.Append(menu3, 'World')
        menu3.Append(112, 'Delete Overworld')
        self.Bind(wx.EVT_MENU, self.DeleteOverworld, id=112)
        menu3.Append(113, 'Delete Nether')
        self.Bind(wx.EVT_MENU, self.DeleteNether, id=113)
        menu3.Append(114, 'Delete The End')
        self.Bind(wx.EVT_MENU, self.DeleteTheEnd, id=114)

        self.SetMenuBar(menu_bar)

        self.pnl = wx.Panel(self)
        self.SetBackgroundColour(wx.LIGHT_GREY)
        self.before = wx.StaticText(self.pnl, label = 'Use only when opening the server for the first time before starting it')
        self.before.SetPosition((5,10))
        # self.after = wx.StaticText(self.pnl, label = 'Set after startup')
        # self.after.SetPosition((5,100))
        button_height_before = 30
        # button_height_after = 120
        self.start = wx.Button(self.pnl, id=111, label = 'Run the server', pos =(650,350), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonStart, id=111)
        self.start.SetBackgroundColour(wx.Colour(255,255,200))
        self.setup = wx.Button(self.pnl, id=11, label = 'Download bukkit/tools', pos =(0,button_height_before), size =(150,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonSetup, id=11)
        self.eula = wx.Button(self.pnl, id=12, label = 'Agree EULA', pos =(160,button_height_before), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonEULA, id=12)

        self.Centre()
        


    def ButtonStart(self, event):
        start_server.RunServer()


    def Settings(self,event):
        print('Settings activated.')
        frame = check.CheckFrame(self, -1, 'Server Settings')
        frame.SetMaxSize(wx.Size(740,375))
        frame.SetMinSize(wx.Size(740,375))
        frame.Show()

    def Quit(self, event):
        dialog = wx.MessageDialog(self, 'Are you sure want to quit?', 'Warning', wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            quit(0)
        else:
            pass
        dialog.Destroy()

    def ButtonSetup(self, event):
        install.RunInstall()

    def ButtonEULA(self, event):
        activate_eula.ActivateEula()
        dialog = wx.MessageDialog(None, 'You have agreed to EULA.', 'Message', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def OpenProperties(self, event):
        os.system('start notepad.exe server.properties')
    
    def OpenOp(self, event):
        os.system('start notepad.exe ops.json')

    def OpenBan(self,event):
        os.system('start notepad.exe banned-players.json')
    
    def OpenBanIP(self,event):
        os.system('start notepad.exe banned-ips.json')
    
    def OpenWhiteList(self,event):
        os.system('start notepad.exe whitelist.json')

    def OpenBukkit(self,event):
        os.system('start notepad.exe bukkit.yml')

    def OpenCommand(self, event):
        os.system('start notepad.exe commands.yml')

    def OpenSpigot(self, event):
        os.system('start notepad.exe spigot.yml')

    def OpenHelp(self, event):
        os.system('start notepad.exe help.yml')
    

    def DeleteOverworld(self, event):
        try:
            shutil.rmtree(r'world')
        except:
            dialog = wx.MessageDialog(self, 'Overworld map folder does not exist in the current directory.', 'Error', wx.OK)
        else:
            dialog = wx.MessageDialog(self, 'Overworld map files in the current directory have been deleted successfully.', 'Notice', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()


    def DeleteNether(self, event):
        try:
            shutil.rmtree(r'world_nether')
        except:
            dialog = wx.MessageDialog(self, 'Nether map folder does not exist in the current directory.', 'Error', wx.OK)
        else:
            dialog = wx.MessageDialog(self, 'Nether map files in the current directory have been deleted successfully.', 'Notice', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def DeleteTheEnd(self, event):
        try:
            shutil.rmtree(r'world_the_end')
        except:
            dialog = wx.MessageDialog(self, 'The End map folder does not exist in the current directory.', 'Error', wx.OK)
        else:
            dialog = wx.MessageDialog(self, 'The End map files in the current directory have been deleted successfully.', 'Notice', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()
 

def RunMain():
    app = wx.App()
    frame = MainFrame(None, -1, 'Minecraft Server Manager') # id = -1 to put initial value
    frame.SetMaxSize(wx.Size(800,600))
    frame.SetMinSize(wx.Size(800,600))
    frame.Show()
    app.MainLoop()


RunMain()
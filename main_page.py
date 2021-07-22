import wx, os
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
        menu.Append(101,'Settings')
        self.Bind(wx.EVT_MENU, self.Settings, id=101)
        menu.Append(102, 'Quit')
        self.Bind(wx.EVT_MENU, self.Quit, id=102)
        self.SetMenuBar(menu_bar)

        self.pnl = wx.Panel(self)
        self.before = wx.StaticText(self.pnl, label = 'Use only when opening the server for the first time before starting it')
        self.before.SetPosition((5,10))
        self.after = wx.StaticText(self.pnl, label = 'Set after startup')
        self.after.SetPosition((5,100))
        button_height_before = 30
        button_height_after = 120
        self.start = wx.Button(self.pnl, id=111, label = 'Run the server', pos =(650,350), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonStart, id=111)
        self.setup = wx.Button(self.pnl, id=11, label = 'Download bukkit/tools', pos =(0,button_height_before), size =(150,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonSetup, id=11)
        self.eula = wx.Button(self.pnl, id=12, label = 'Agree EULA', pos =(160,button_height_before), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonEULA, id=12)
        self.server_properties = wx.Button(self.pnl, id=2, label = 'Open Server.properties', pos =(0,button_height_after), size =(130,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonProperties, id=2)
        self.ops = wx.Button(self.pnl, id=3, label = 'Open Op list', pos =(140,button_height_after), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonOp, id=3)
        self.ban = wx.Button(self.pnl, id=4, label = 'Open Ban-player list', pos =(250,button_height_after), size =(130,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonBan, id=4)
        self.banip = wx.Button(self.pnl, id=5, label = 'Open Ban-ip list', pos =(390,button_height_after), size =(110,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonBanIP, id=5)
        self.whitelist = wx.Button(self.pnl, id=6, label = 'Open Whitelist', pos =(510,button_height_after), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonWhiteList, id=6)

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

    def ButtonProperties(self, event):
        os.system('start notepad.exe server.properties')
    
    def ButtonOp(self, event):
        os.system('start notepad.exe ops.json')

    def ButtonBan(self,event):
        os.system('start notepad.exe banned-players.json')
    
    def ButtonBanIP(self,event):
        os.system('start notepad.exe banned-ips.json')
    
    def ButtonWhiteList(self,event):
        os.system('start notepad.exe whitelist.json')


 
def RunMain():
    app = wx.App()
    frame = MainFrame(None, -1, 'Minecraft Server Manager') # id = -1 to put initial value
    frame.SetMaxSize(wx.Size(800,600))
    frame.SetMinSize(wx.Size(800,600))
    frame.Show()
    app.MainLoop()


RunMain()
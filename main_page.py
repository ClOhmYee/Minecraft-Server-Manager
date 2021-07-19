import wx, os
import check, DataTool, start_server, activate_eula  # use detail.py, DataTool.py, start_server.py, activate_eula.py

global xms, xmx, jar
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
        self.button1 = wx.Button(self.pnl, id=111, label = 'Run the server', pos =(650,350), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonStart, id=111)
        self.button2 = wx.Button(self.pnl, id=1, label = 'Agree EULA', pos =(10,10), size =(100,50))
        self.Bind(wx.EVT_BUTTON, self.ButtonEULA, id=1)

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
    
    def ButtonEULA(self, event):
        activate_eula.ActivateEula()
        dialog = wx.MessageDialog(None, 'You have agreed to EULA.', 'Message', wx.OK)
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
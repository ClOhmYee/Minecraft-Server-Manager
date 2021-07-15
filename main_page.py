import os
import wx
import check
import DataTool

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
        self.show_status = wx.StaticText(self, label = 'xms = {}, xmx = {}, jar = {}'.format(xms,xmx,jar))
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



def RunMain():
    app = wx.App()
    frame = MainFrame(None, -1, 'Minecraft Server Manager') # id = -1 to put initial value
    frame.Show()
    app.MainLoop()

RunMain()



# number = input('Enter : ')

# if number == '1':
#     boot_path = os.getcwd() + '\start_server.py'
#     exec(open(boot_path).read())
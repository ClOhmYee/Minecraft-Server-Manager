import os
import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        menu_bar = wx.MenuBar()
        menu = wx.Menu()
        menu_bar.Append(menu, 'Setting')
        menu.Append(101,'Adjust RAM allocation')
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.RAM_allocation, id=101)

    def RAM_allocation(self,event):
        print('RAM allocation activated.')
        frame = CheckFrame(self, -1, 'Server RAM allocation')
        frame.Show()



class CheckFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))



def run():
    app = wx.App()
    frame = MainFrame(None, -1, 'Minecraft Server Manager') # id = -1 to put initial value
    frame.Show()
    app.MainLoop()

run()



# number = input('Enter : ')

# if number == '1':
#     boot_path = os.getcwd() + '\start_server.py'
#     exec(open(boot_path).read())
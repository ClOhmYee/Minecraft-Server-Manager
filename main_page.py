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
        menu.Append(102, 'Quit')
        self.Bind(wx.EVT_MENU, self.Quit, id=102)

    def RAM_allocation(self,event):
        print('RAM allocation activated.')
        frame = CheckFrame(self, -1, 'Server RAM allocation')
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
        wx.Frame.__init__(self, parent, id, title, size=(800,600))
        self.button = wx.Button(self, id=1, label = '1') #parent, id(ID_ANY), label, pos, size, style, validator, name
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, id=1) #event, handler, source, id
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.button, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def ButtonClick(self, event):
        print('Button 1 clicked')


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
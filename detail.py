import wx
import os

data_path = os.path.dirname(__file__)+'\data'




# -----------------------------------xms-----------------------------------
class DetailXmsInfo(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,170))

        self.panel = wx.Panel(self)
        self.xms = wx.StaticText(self.panel, label = "Please enter the minimum RAM allocation you want (unit : MB) :")
        self.xms.SetPosition((10,50))
        self.g_xms = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        self.g_xms.SetPosition((365,50))

        self.button = wx.Button(self.panel, label = "Done")
        self.button.SetPosition((400,100))
        self.button.Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.g_xms.Bind(wx.EVT_TEXT_ENTER, self.ButtonClick)

    
    def ButtonClick(self,event):
        global xms
        xms_value = self.g_xms.GetValue()
        xms = '-Xms'+str(xms_value)+'M'
        print(xms)
        dialog = wx.MessageDialog(self, 'Are you sure want to allocate your server minimum RAM : {}MB?'.format(xms_value), 'Warning', wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            xms_file = open(data_path+'\data_xms.txt', 'w')
            xms_file.write(xms)
            xms_file.close()
            self.Close() # close the detail page
        else:
            pass
        dialog.Destroy()




# -----------------------------------xmx-----------------------------------
class DetailXmxInfo(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,170))

        self.panel = wx.Panel(self)
        self.xmx = wx.StaticText(self.panel, label = "Please enter the maximum RAM allocation you want (unit : MB) :")
        self.xmx.SetPosition((10,50))
        self.g_xmx = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        self.g_xmx.SetPosition((365,50))

        self.button = wx.Button(self.panel, label = "Done")
        self.button.SetPosition((400,100))
        self.button.Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.g_xmx.Bind(wx.EVT_TEXT_ENTER, self.ButtonClick)

    
    def ButtonClick(self,event):
        global xmx
        xmx_value = self.g_xmx.GetValue()
        xmx = '-Xmx'+str(xmx_value)+'M'
        print(xmx)
        dialog = wx.MessageDialog(self, 'Are you sure want to allocate your server maximum RAM : {}MB?'.format(xmx_value), 'Warning', wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            xmx_file = open(data_path+'\data_xmx.txt','w')
            xmx_file.write(xmx)
            xmx_file.close()
            self.Close() # close the detail page
        else:
            pass
        dialog.Destroy()
    



def RunXms():
    app = wx.App()
    frame = DetailXmsInfo(None, -1, 'RAM allocation test (xms)') # xms test
    frame.Show()
    app.MainLoop()

def RunXmx():
    app = wx.App()
    frame = DetailXmxInfo(None, -1, 'RAM allocation test (xmx)') # xmx test
    frame.Show()
    app.MainLoop()

# type RunXms() or RunXmx() below to test classes.
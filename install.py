import os, wx
import DataTool




class InstallFrame(wx.Frame):
    def __init__(self, parent, id, title):
        os.chdir(DataTool.base_path)
        wx.Frame.__init__(self, parent, id, title, size=(500,190))
        self.version = wx.StaticText(self, label = 'Enter the version of the server you want to start : ')
        self.version.SetPosition((10,15))
        self.g_version = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.g_version.SetPosition((280,12))
        self.button = wx.Button(self, label = 'Done')
        self.button.SetPosition((400,12))
        self.button.Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.g_version.Bind(wx.EVT_TEXT_ENTER, self.ButtonClick)
        self.warning = wx.StaticText(self, label = 'Once you have completed entering the version, you will download server tools. \nPlease DO NOT MANIPULATE the program until you receive a notification message.')
        self.warning.SetPosition((10,70))
        self.warning2 = wx.StaticText(self, label = 'This is a one-time operation. \nIf you have already downloaded it, you do not need to reinstall it.')
        self.warning2.SetPosition((10,110))

        self.Centre()

    def ButtonClick(self, event):
        dialog = wx.MessageDialog(self, 'Are you sure want to configure the server for version {}?'.format(self.g_version.GetValue()), 'Warning', wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            version_value = self.g_version.GetValue()
            os.system('curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar')
            os.system('java -jar BuildTools.jar --rev {}'.format(version_value))
            dialog = wx.MessageDialog(self, 'Download complete.', 'Notification', wx.OK)
            dialog.ShowModal()
            self.Close() # close page
        else:
            pass
        dialog.Destroy()


def RunInstall():
    app = wx.App()
    frame = InstallFrame(None, -1, 'Installation')
    frame.SetMaxSize(wx.Size(500,190))
    frame.SetMinSize(wx.Size(500,190))
    frame.Show()
    app.MainLoop()

# RunInstall()
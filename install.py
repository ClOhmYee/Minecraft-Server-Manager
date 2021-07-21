import os
import wx




os.system('curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar')

class InstallFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(450,70))
        self.version = wx.StaticText(self, label = 'Enter the version of the server you want to start : ')
        self.version.SetPosition((5,10))
        self.g_version = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.g_version.SetPosition((280,7))
        self.button = wx.Button(self, label = 'Done')
        self.button.SetPosition((150,70))
        self.button.Bind(wx.EVT_BUTTON, self.ButtonClick)
        self.g_version.Bind(wx.EVT_TEXT_ENTER, self.ButtonClick)

    def ButtonClick(self, event):
        dialog = wx.MessageDialog(self, 'Are you sure want to configure the server for version {}?'.format(self.g_version.GetValue()), 'Warning', wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            version_value = self.g_version.GetValue()
            os.system('java -jar BuildTools.jar --rev {}'.format(version_value))
            self.Close() # close page
        else:
            pass
        dialog.Destroy()


def RunInstall():
    app = wx.App()
    frame = InstallFrame(None, -1, 'Installation')
    frame.SetMaxSize(wx.Size(450,70))
    frame.SetMinSize(wx.Size(450,70))
    frame.Show()
    app.MainLoop()

RunInstall()
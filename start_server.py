import os, wx
import DataTool

app = wx.App()
os.chdir(DataTool.base_path)

def RunServer():
    try: # import all data to boot server
        file_xms = open(DataTool.data_path+'\data_xms.txt','r')
        xms = file_xms.read()
        file_xms.close()
        file_xmx = open(DataTool.data_path+'\data_xmx.txt','r')
        xmx = file_xmx.read()
        file_xmx.close()
        file_jar = open(DataTool.data_path+'\data_jar.txt','r')
        jar = file_jar.read()
        file_jar.close()
    except:
        dialog = wx.MessageDialog(None, 'Please enter all information before running the server.\nGo to Menu > Settings > Input all values (xms, xmx, jar)', 'Error', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()
    else:
        cmd = 'java {} {} -jar {}'.format(xms, xmx, jar)
        print('Starting the server . . .')
        print(cmd)
        os.system(cmd)


# RunServer()
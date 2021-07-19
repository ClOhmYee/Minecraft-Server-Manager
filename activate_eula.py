import DataTool

file_eula = open(DataTool.base_path+'\eula.txt','w')
file_eula.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\neula=TRUE')
file_eula.close()
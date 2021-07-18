import os

base_path = os.path.dirname(__file__)
data_path = os.path.dirname(__file__)+'\data'

def SaveXms(xms):
    file_xms = open(data_path+'\data_xms.txt','w')
    file_xms.write(xms)
    file_xms.close()

def SaveXmx(xmx):
    file_xmx = open(data_path+'\data_xmx.txt','w')
    file_xmx.write(xmx)
    file_xmx.close()

def SaveJar(jar):
    file_jar = open(data_path+'\data_jar.txt','w')
    file_jar.write(jar)
    file_jar.close()
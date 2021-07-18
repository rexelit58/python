#Absolute path
    #windows
        #c:\Program Files\Microsoft
    #linux
        #/usr/local/bin
from pathlib import Path
path=Path("ecommerce")
print(path.exists())
path1=Path("ecommerce12")
print(path1.exists())
path2=Path("emails")
#path2.mkdir()
path2.rmdir()
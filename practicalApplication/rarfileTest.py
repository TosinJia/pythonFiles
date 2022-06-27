import rarfile

path ="E:\\test.rar"
path ="E:\\test-password.rar"
with rarfile.RarFile(path) as rf:
    rf.extractall(pwd="123456")

# Path add C:\Program Files\WinRAR
import os
import subprocess

#https://www.cnblogs.com/gexbooks/p/12673785.html
cmd = "adb devices"
# cmd = "adb shell pm list packages | findstr alibaba"
print("一、os.system()")
result1 = os.system(cmd)
print(result1)

print("二、os.popen()")
result2 = os.popen(cmd).read()
print(result2)

print("三、subprocess.Popen()")
res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result3 = res.stdout.read()
res.wait()
res.stdout.close()
print(result3)

print("四、subprocess.getstatusoutput()")
result4 = subprocess.getstatusoutput(cmd)
print(result4)
#import subprocess
#process = subprocess.Popen('adb shell input tap 14 1402')
#print(process)

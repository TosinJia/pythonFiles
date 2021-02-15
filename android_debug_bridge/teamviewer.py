import os
import subprocess
import time

#import helloadb02
from helloadb02 import *

cmd = "adb devices"
# cmd = "adb shell am start -n com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity"
# cmd = "adb shell am force-stop com.teamviewer.quicksupport.market"
#com.huawei.android.launcher/.unihome.UniHomeLauncher
# cmd = "adb shell dumpsys activity | findstr mF"
# cmd = "adb shell input tap 864 1093"
# res = adb_shell1(cmd)
# print(res)

# 注：奇兔连接成功后，执行 adb server version (31) doesn't match this client (41); killing...\nerror: unknown host service\ncould not read ok from ADB Server\n* failed to start daemon\nadb.exe: failed to check server version: cannot connect to daemon
## 关闭奇兔重新连接后，正常执行

def curTime(seconds):
    curTime = time.localtime(seconds)
    format_time = '%Y-%m-%d %H:%M:%S'
    return time.strftime(format_time, curTime)


# 设备连接



# 判断设备是否连接
while 1:
    print(curTime(time.time())+" 检测设备是否连接")
    cmd = "adb devices"
    res = adb_shell4(cmd)
    print(res)
    if "EJL4C17706001732" in res[1]:
        break;
    else:
        time.sleep(5)

# 启动APP
app_package = "com.teamviewer.quicksupport.market"
app_activity = "com.teamviewer.quicksupport.ui.QSActivity"
show_cur_activity_cmd = "adb shell dumpsys activity | findstr mF"
while 1:
    print("{0} 启动APP[{1}]".format(curTime(time.time()), app_activity))
    start_cmd = "adb shell am start -n {0}/{1}".format(app_package, app_activity)
    start_res = adb_shell4(start_cmd)
    # print(start_res)

    # 检测是否启动成功

    show_cur_activity_res = adb_shell4(show_cur_activity_cmd)
    # print(show_cur_activity_res, show_cur_activity_res[1])
    if("{0}/{1}".format(app_package, app_activity) in show_cur_activity_res[1]):
        print("{0} {1} APP启动成功".format(curTime(time.time()), app_activity))
        break
    else:
        print("{0} {1} APP启动失败".format(curTime(time.time()), app_package))
    time.sleep(5)

# 连接设备，点击允许
while 1:
    print("{0} 尝试点击允许".format(curTime(time.time())))
    show_cur_activity_res = adb_shell4(show_cur_activity_cmd)
    if "{0}/{1}".format(app_package, app_activity) in show_cur_activity_res[1]:
        cmd = "adb shell input tap 864 1093"
        adb_shell4(cmd)
    else:
        print("{0} 连接成功".format(curTime(time.time())))
        break
    time.sleep(10)


stop_cmd = "adb shell am force-stop {0}".format(app_package)
# stop_res = adb_shell4(stop_cmd)


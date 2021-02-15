[TOC]

## AndroidDebugBridge
### 下载地址
- https://dl.google.com/android/repository/platform-tools_r30.0.5-windows.zip


### Python
- [Python Python3 执行 adb shell 命令详解](https://testerhome.com/topics/20497)
```
import os
import subprocess

# 方法一：os.system()
# 返回值：返回对应状态码，且状态码只会有0(成功)、1、2。
# 其它说明：os.system()的返回值并不是执行程序的返回结果。而是一个16位的数，它的高位才是返回码。也就是说os.system()执行返回256即 0×0100，返回码应该是其高位0×01即1。所以要获取它的状态码的话，需要通过>>8移位获取。
def adb_shell1(cmd):
    exit_code = os.system(cmd)
    return exit_code >> 8


# # 方法二：os.popen()
# # 返回值：返回脚本命令输出的内容
# # 其它说明：os.popen()可以实现一个“管道”，从这个命令获取的值可以继续被调用。而os.system不同，它只是调用，调用完后自身退出，执行成功直接返回个0。
def adb_shell2(cmd):
    result = os.popen(cmd).read()
    return result


# # 方法三：subprocess.Popen()
# # 返回值：Popen类的构造函数，返回结果为subprocess.Popen对象，脚本命令的执行结果可以通过stdout.read()获取。
def adb_shell3(cmd):
    res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = res.stdout.read()
    res.wait()
    res.stdout.close()
    return result


# 方法四：subprocess.getstatusoutput()
# 返回值：返回是一个元组，如果成功，返回(0, 'xxx')；如果失败，返回(1, 'xxx')
def adb_shell4(cmd):
    result = subprocess.getstatusoutput(cmd)
    return result


cmd = "adb devices"
# cmd = "adb shell pm list packages | findstr alibaba"
result1 = adb_shell1(cmd)
result2 = adb_shell2(cmd)
result3 = adb_shell3(cmd)
result4 = adb_shell4(cmd)

print(result1, result2, result3, result4)
```
#### 实操
- [python+adb实现自动化获取手机信息](https://www.cnblogs.com/sgfg-1314/p/10400791.html)
- https://www.cnblogs.com/zzpython/archive/2020/07/25/13377508.html


### 常见指令
- [ADB——命令大全](https://www.cnblogs.com/zhuminghui/p/10457316.html)
- [awesome-adb](https://github.com/mzlogin/awesome-adb)

#### 常用
##### 获取当前activity名称
```
adb shell dumpsys activity | findstr "mF"
```
##### 屏幕分辨率
```
adb devices
adb -s EJL4C17706001732 shell wm size
```
##### 启动停止
```
adb start-server # 启动（一般无需手动执行此命令，在运行 adb 命令时若发现 adb server 没有启动会自动调起。）
adb kill-server    # 停止
adb version        # 查看adb版本号
```





#### 常见应用程序 包名 活动名

应用 | 信息
---|---
teamviewer | com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity
钉钉 | com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity

#### 应用管理
- [ADB——管理应用](https://www.cnblogs.com/zhuminghui/p/10489486.html)

##### 查看应用列表
> adb shell pm list packages [-f] [-d] [-e] [-s] [-3] [-i] [-u] [--user USER_ID] [FILTER]


参数 | 显示列表
---|---
无 | 所有应用
-f | 显示应用关联的 apk 文件
-d | 只显示 disabled 的应用
-e | 只显示 enabled 的应用
-s | 只显示系统应用
-3 | 只显示第三方应用
-i | 显示应用的 installer
-u | 包含已卸载应用
<FILTER> | 包名包含<FILTER>的字符串


```
# 查看所有应用
adb shell pm list packages

# 查看某个包名中包含指定字符的应用
>adb shell pm list packages alibaba
package:com.alibaba.android.rimet

>adb shell pm list packages | grep alibaba
'grep' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

>adb shell pm list packages | findstr alibaba
package:com.alibaba.android.rimet
```
##### 查看前台Activity
```
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell dumpsys activity activities | findstr LaunchHomeActivity
      intent={act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=com.alibaba.android.rimet/.biz.LaunchHomeActivity}
      realActivity=com.alibaba.android.rimet/.biz.LaunchHomeActivity
      Activities=[ActivityRecord{ee8faad u0 com.alibaba.android.rimet/.biz.LaunchHomeActivity t83}]
      * Hist #0: ActivityRecord{ee8faad u0 com.alibaba.android.rimet/.biz.LaunchHomeActivity t83}
          Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=com.alibaba.android.rimet/.biz.LaunchHomeActivity bnds=[12,84][276,367] }
          realActivity=com.alibaba.android.rimet/.biz.LaunchHomeActivity
        Run #4: ActivityRecord{ee8faad u0 com.alibaba.android.rimet/.biz.LaunchHomeActivity t83}
    mResumedActivity: ActivityRecord{ee8faad u0 com.alibaba.android.rimet/.biz.LaunchHomeActivity t83}
  mFocusedActivity: ActivityRecord{ee8faad u0 com.alibaba.android.rimet/.biz.LaunchHomeActivity t83}
```

##### 查看运行的services
```
adb shell dumpsys activity services com.alibaba.android.rimet
```
##### 查看应用信息
```
adb shell dumpsys package com.alibaba.android.rimet
```
##### 查看应用安装路径
```
>adb shell pm path com.alibaba.android.rimet
package:/data/app/com.alibaba.android.rimet-1/base.apk
```

#### 应用交互

##### 启动应用 / 调起Activity

```
adb shell am start -n {包(package)名}/{包名}.{活动(activity)名称}
```
##### 强制停止应用
```
adb shell am force-stop {包(package)名}
```

#### 模拟按键输入
##### 亮屏、熄屏
```
adb shell input keyevent 224 # 点亮屏幕
adb shell input keyevent 223 # 熄灭屏幕

adb shell input keyevent 26 # 电源键
adb shell input keyevent 82 # 菜单键
adb shell input keyevent 3 # HOME 键
adb shell input keyevent 4 # 返回键
adb shell input keyevent 24 # 音量+
adb shell input keyevent 25 # 音量-
adb shell input keyevent 164 # 静音 
```
- [ADB——keyevent命令](https://www.cnblogs.com/zhuminghui/p/10470865.html)

##### 触击、滑动
```
# 触击屏幕
adb shell input tap <X> <Y> # x，y为坐标位置

# 滑动屏幕  四个参数：起始点x坐标 起始点y坐标 结束点x坐标 结束点y坐标。
adb shell input swipe 300 1000 300 500 # 向上滑动
adb shell input swipe 300 100 300 1000 # 向下滑动
adb shell input swipe 1000 500 200 500 # 向左滑动
adb shell input swipe 200 500 1000 500 # 向右滑动
```
#### 查看日志
##### 按级别过滤日志


标识 | 描述
---|---
V | Verbose（最低，输出得最多）
D | Debug
I | Info
W | Warning
E | Error
F | Fatal
S | Silent（最高，啥也不输出）

```
adb logcat *:W # 注： 在 macOS 下需要给 *:W 这样以 * 作为 tag 的参数加双引号，如 adb logcat "*:W"，不然会报错 no matches found: *:W
```
##### 按 tag 和级别过滤日志
```
# <filter-spec> 可以由多个 <tag>[:priority] 组成。

# 比如，下面命令表示输出 tag ActivityManager 的 Info 以上级别日志，输出 tag MyApp 的 Debug 以上级别日志，及其它 tag 的 Silent 级别日志（即屏蔽其它 tag 日志）
adb logcat ActivityManager:I MyApp:D *:S
```

##### 清空
```
adb logcat -c
```

#### 其他实用功能
##### 屏幕截图
```
# 如果 adb 版本较老，无法使用 exec-out 命令，建议更新 adb 版本。若无法更新使用如下步骤：
# 先截图保存到设备里
>adb shell screencap -p /sdcard/sc.png

# # 然后将 png 文件导出到电脑：
>adb pull /sdcard/sc.png
9194 KB/s (169469 bytes in 0.018s)

```
##### 重启手机
```
adb reboot
```

#### 其他ADB shell命令 
##### 查看进程
列名 | 含义
---|---
USER | 所属用户
PID | 进程 ID
PPID | 父进程 ID
NAME | 进程名

```
>adb shell ps
USER      PID   PPID  VSIZE  RSS   WCHAN              PC  NAME
root      1     0     21464  1928  SyS_epoll_ 0000000000 S /init
root      2     0     0      0       kthreadd 0000000000 S kthreadd
root      3     2     0      0     smpboot_th 0000000000 S ksoftirqd/0
root      4     2     0      0     worker_thr 0000000000 S kworker/0:0
root      5     2     0      0     worker_thr 0000000000 S kworker/0:0H
root      6     2     0      0     msm_mpm_wo 0000000000 D kworker/u16:0
root      7     2     0      0     rcu_gp_kth 0000000000 S rcu_preempt
root      8     2     0      0     rcu_gp_kth 0000000000 S rcu_sched
```
##### 查看实时资源占用情况
列名 | 含义
---|---
PID | 进程 ID
PR | 优先级
CPU% | 当前瞬间占用 CPU 百分比
S | 进程状态（R=运行，S=睡眠，T=跟踪/停止，Z=僵尸进程）
VSS | Virtual Set Size 虚拟耗用内存（包含共享库占用的内存）
RSS | Resident Set Size 实际使用物理内存（包含共享库占用的内存）
PCY | 调度策略优先级，SP_BACKGROUND/SPFOREGROUND
UID | 进程所有者的用户 ID
NAME | 进程名


> Usage: top [ -m max_procs ] [ -n iterations ] [ -d delay ] [ -s sort_column ] [ -t ] [ -h ]

命令行参数 | 含义
---|---
-m num | 最多显示多少个进程
-n num | 刷新多少次后退出
-d num | 刷新时间间隔（单位秒，默认值 5）
-s col | 按某列排序（可用 col 值：cpu, vss, rss, thr）
-t | 显示线程信息
-h | 显示帮助文档

```
>adb shell top -m 10 -s cpu -t
User 5%, System 11%, IOW 0%, IRQ 1%
User 11 + Nice 0 + Sys 22 + Idle 155 + IOW 0 + IRQ 1 + SIRQ 2 = 191

  PID   TID USER     PR  NI CPU% S     VSS     RSS PCY Thread          Proc
 8222  8222 shell    20   0  10% R   9136K   3172K  fg top             top
 5736  5736 shell    20   0   2% S  27940K    596K  fg adbd            /sbin/adbd
 5736  5742 shell    20   0   1% S  27940K    596K  fg ->transport     /sbin/adbd
 5736  8217 shell    20   0   1% S  27940K    600K  fg service 20      /sbin/adbd
 5736  5743 shell    20   0   0% S  27940K    600K  fg <-transport     /sbin/adbd
 1814  2191 system   20   0   0% S 2664732K 197248K  fg HwNormalizedAut system_server
 7848  7848 root     20   0   0% S      0K      0K  fg kworker/7:1
 8218  8218 shell    20   0   0% S  36524K   6164K  fg screencap       screencap
   25    25 root     20   0   0% S      0K      0K  fg rcuop/2
   11    11 root     20   0   0% S      0K      0K  fg rcuos/0

```

### 实操
#### teamviewer
```
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input keyevent 3

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am start -n com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity
Starting: Intent { cmp=com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity }

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 864 1093

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am force-stop com.teamviewer.quicksupport.market
```

#### 钉钉
```
# 点亮屏幕
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input keyevent 224
# 滑动解锁
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input swipe 540 1800 1000 1800

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
Starting: Intent { cmp=com.alibaba.android.rimet/.biz.LaunchHomeActivity }
# 点击密码输入框
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 160 860
# 输入密码
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input text dd123456
# 收起键盘
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 1016 928
# 点击登录
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 532 1036
# 选中工作台
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 540 1700
# 上滑
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input swipe 300 1500 300 500
# 点击考勤打卡
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 100 900
# 点击上下班打卡
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 520 1100
# 点击返回
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input keyevent 4
# 关闭程序
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am force-stop com.alibaba.android.rimet

```

```

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell
HWMLA:/ $ pm list package | grep alibaba
pm list package | grep alibaba
package:com.alibaba.android.rimet
HWMLA:/ $ exit
exit

获取当前activity名称
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell dumpsys activity | findstr "mF"
  mFullscreen=true
    mFullscreen=true
    mFullscreen=true
    mFullscreen=true
    mFullscreen=true
    mFullscreen=true
    mFullscreen=true
    mFullscreen=true
  mFullscreen=true
    mFullscreen=true
    mFullscreen=true
  mFocusedActivity: ActivityRecord{9fdd962 u0 com.alibaba.android.rimet/.biz.LaunchHomeActivity t47}
  mFocusedStack=ActivityStack{f59c873 stackId=1, 8 tasks} mLastFocusedStack=ActivityStack{f59c873 stackId=1, 8 tasks}

adb启动 应用程序

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity
Starting: Intent { cmp=com.alibaba.android.rimet/.biz.LaunchHomeActivity }

adb停止应用程序
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am force-stop com.alibaba.android.rimet

Teamviewer
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell dumpsys activity | findstr "mF"
  mFullscreen=true
    mFullscreen=true
  mFullscreen=true
    mFullscreen=true
    mFullscreen=true
  mFocusedActivity: ActivityRecord{5aaeb5f u0 com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity t29}
  mFocusedStack=ActivityStack{f59c873 stackId=1, 2 tasks} mLastFocusedStack=ActivityStack{f59c873 stackId=1, 2 tasks}


D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am force-stop com.teamviewer.quicksupport.market

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am start -n com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity
Starting: Intent { cmp=com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity }

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 864 1093



==============

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb logcat -c

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb logcat * | find "teamviewer"
02-04 12:17:58.399 10789 10789 I appproc : Command=app_process /system/bin com.android.commands.am.Am start -n com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity
02-04 12:17:59.094  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market
02-04 12:18:00.820 10804 10804 I art     : Rejecting re-init on previously-failed class java.lang.Class<com.teamviewer.incomingremotecontrolsonyenterpriselib.method.RcMethodSonyEnterprise$3>: java.lang.NoClassDefFoundError: Failed resolution of: Lcom/sonymobile/enterprise/DeviceControl$DeviceControlSessionListener;
02-04 12:18:00.820 10804 10804 I art     :   at void com.teamviewer.quicksupport.ui.QSActivity.a(boolean) (SourceFile:18)
02-04 12:18:00.820 10804 10804 I art     :   at void com.teamviewer.quicksupport.ui.QSActivity.D() (SourceFile:3)
02-04 12:18:00.820 10804 10804 I art     :   at void com.teamviewer.quicksupport.ui.QSActivity.onCreate(android.os.Bundle) (SourceFile:17)
02-04 12:18:00.820 10804 10804 I art     : Caused by: java.lang.ClassNotFoundException: Didn't find class "com.sonymobile.enterprise.DeviceControl$DeviceControlSessionListener" on path: DexPathList[[zip file "/data/app/com.teamviewer.quicksupport.market-1/base.apk"],nativeLibraryDirectories=[/data/app/com.teamviewer.quicksupport.market-1/lib/arm64, /data/app/com.teamviewer.quicksupport.market-1/base.apk!/lib/arm64-v8a, /system/lib64, /vendor/lib64, /system/vendor/lib64, /product/lib64]]
02-04 12:18:00.820 10804 10804 I art     :   at void com.teamviewer.quicksupport.ui.QSActivity.a(boolean) (SourceFile:18)
02-04 12:18:00.820 10804 10804 I art     :   at void com.teamviewer.quicksupport.ui.QSActivity.D() (SourceFile:3)
02-04 12:18:00.820 10804 10804 I art     :   at void com.teamviewer.quicksupport.ui.QSActivity.onCreate(android.os.Bundle) (SourceFile:17)
02-04 12:18:01.023  1767  1880 I ActivityManager: Displayed com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity: +2s494ms
02-04 12:18:15.168  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market
02-04 12:18:15.170  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=1  WEBRESENDSEGS=0  WEBRECVSEGS=1  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=8  WEBRTTSEGS=1  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:18:20.177  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am start -n com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity
Starting: Intent { cmp=com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity }





02-04 12:18:25.179  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market
02-04 12:18:30.188  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market
02-04 12:18:30.189  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=2  WEBRESENDSEGS=0  WEBRECVSEGS=1  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=6  WEBRTTSEGS=1  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:18:35.183  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market
02-04 12:18:35.184  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=1  WEBRESENDSEGS=0  WEBRECVSEGS=1  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=9  WEBRTTSEGS=1  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:18:41.241  1767  2162 E HwCHRWebMonitor: running processName=com.teamviewer.quicksupport.market

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 864 1093



02-04 12:18:59.343  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86856935
02-04 12:18:59.343  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[1]
02-04 12:19:03.384  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86860976
02-04 12:19:03.384  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[1, 2]
02-04 12:19:03.528 10804 10900 I HwResourcesImpl: load icon id : 7f080087, pkgName : com.teamviewer.quicksupport.market
02-04 12:19:03.529 10804 10900 I HwResourcesImpl: icon : com.teamviewer.quicksupport.market found in app
02-04 12:19:03.781 10804 10900 I HwResourcesImpl: load icon id : 7f0800f3, pkgName : com.teamviewer.teamviewer.market.mobile
02-04 12:19:03.781 10804 10900 I HwResourcesImpl: icon : com.teamviewer.teamviewer.market.mobile found in app
02-04 12:19:12.286  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=7  WEBRESENDSEGS=0  WEBRECVSEGS=4  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=14  WEBRTTSEGS=3  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:19:22.296  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=3  WEBRESENDSEGS=0  WEBRECVSEGS=2  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=4  WEBRTTSEGS=1  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:19:27.302  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=2  WEBRESENDSEGS=0  WEBRECVSEGS=1  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=4  WEBRTTSEGS=1  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:19:32.305  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=4  WEBRESENDSEGS=0  WEBRECVSEGS=2  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=33  WEBRTTSEGS=2  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]
02-04 12:19:37.313  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=1  WEBRESENDSEGS=0  WEBRECVSEGS=1  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=8  WEBRTTSEGS=1  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]


D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am force-stop com.teamviewer.quicksupport.market

02-04 12:19:41.297 11001 11001 I appproc : Command=app_process /system/bin com.android.commands.am.Am force-stop com.teamviewer.quicksupport.market
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899005
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[2]
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899006
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[2]
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899006
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[2]
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899006
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[2]
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899006
02-04 12:19:41.414  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[2]
02-04 12:19:41.426  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899018
02-04 12:19:41.426  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[]
02-04 12:19:41.426  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899018
02-04 12:19:41.426  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[]
02-04 12:19:41.428  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899020
02-04 12:19:41.428  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[]
02-04 12:19:41.428  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899020
02-04 12:19:41.428  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[]
02-04 12:19:41.428  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification update time:86899020
02-04 12:19:41.428  2546  2636 I AppManager: app:com.teamviewer.quicksupport.market Notification persist:true  Ids:[]
02-04 12:19:43.399  1767  2162 E HwCHRWebMonitor: HwCHRWifiUIDWebSpeed [appName=com.teamviewer.quicksupport.market UID=10141  WEBSENDSEGS=4  WEBRESENDSEGS=0  WEBRECVSEGS=2  WEBERRSEGS=0  WEBOUTRSTS=0  WEBESTABLISRST=0  WEBRTTDURATION=10  WEBRTTSEGS=2  WEBSNDDUPACKS=0  suckTimes=0 recovage_times=0]



D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input keyevent 223

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input keyevent 224

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input swipe 550 1409 550 250


https://webadb.com/


```

#### 实操
```
D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input keyevent 224

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input swipe 550 1409 550 250

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am force-stop com.teamviewer.quicksupport.market

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell am start -n com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity
Starting: Intent { cmp=com.teamviewer.quicksupport.market/com.teamviewer.quicksupport.ui.QSActivity }

D:\Program Files (x86)\奇兔刷机\AdbAdapter>adb shell input tap 864 1093

D:\Program Files (x86)\奇兔刷机\AdbAdapter>
```


### 参考
- https://github.com/mzlogin/awesome-adb#%E6%9F%A5%E7%9C%8B-adb-%E7%89%88%E6%9C%AC
- [ADB——命令大全](https://www.cnblogs.com/zhuminghui/p/10457316.html)

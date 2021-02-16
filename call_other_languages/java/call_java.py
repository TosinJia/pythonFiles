# 引入jpype模块
import jpype
import os


if __name__ == '__main__':
    """
    基本的开发流程如下：
    ①、使用jpype开启jvm
    ②、加载java类
    ③、调用java方法
    ④、关闭jvm（不是真正意义上的关闭，卸载之前加载的类）
    """
    # 1 使用jpype开启虚拟机（在开启jvm之前要加载类路径）
    # 加载打包的jar文件
    jar_path = os.path.join(os.path.abspath("."), "D:\\python_call_java.jar")
    # 获取jvm.dll文件路径
    jvm_path = jpype.getDefaultJVMPath()
    # 开启jvm
    jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=%s" % jar_path)

    # 2 加载java全类名
    java_class = jpype.JClass("com.pythoncalljava.JavaClass")
    # 实例化java对象
    # java_instance = java_class()

    # 3 调用java方法 静态方法，直接使用类名就可以调用方法
    java_class.show()

    # 4 关闭jvm
    jpype.shutdownJVM()

    pass

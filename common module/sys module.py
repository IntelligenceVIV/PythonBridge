# @Time    : 2019/4/25 10:07
# @Author  : Noah
# @File    : sys module.py
# @Software: PyCharm
# @description: sys

# 该模块提供对解释器使用或维护的一些变量的访问以及与解释器强烈交互的函数

import sys

# '__doc__'
print(sys.__doc__)

# Dynamic objects:
#
# argv -- command line arguments; argv[0] is the script pathname if known
print(sys.argv[0])  # F:/Python-Base-Notes/common module/sys module.py

# path -- module search path; path[0] is the script directory, else ''
print(sys.path[0]) # F:\Python-Base-Notes\common module

# modules -- dictionary of loaded modules
#
# displayhook -- called to show results in an interactive session
# excepthook -- called to handle any uncaught exception other than SystemExit
#   To customize printing in an interactive session or to install a custom
#   top-level exception handler, assign other functions to replace these.
#
# stdin -- standard input file object; used by input()
# stdout -- standard output file object; used by print()
# stderr -- standard error object; used for error messages
#   By assigning other file objects (or objects that behave like files)
#   to these, it is possible to redirect all of the interpreter's I/O.
#
# last_type -- type of last uncaught exception
# last_value -- value of last uncaught exception
# last_traceback -- traceback of last uncaught exception
#   These three are only available in an interactive session after a
#   traceback has been printed.
#
# Static objects:
#
# builtin_module_names -- tuple of module names built into this interpreter
# (一个字符串元组)给出了编译到此Python解释器中的所有模块的名称 => sys.builtin_module_names()

# copyright -- copyright notice pertaining to this interpreter
# 与此解释器相关的版权声明

# exec_prefix -- prefix used to find the machine-specific Python library
# 用于查找特定于机器的Python库的前缀

# executable -- absolute path of the executable binary of the Python interpreter
# Python解释器的可执行二进制文件的绝对路径

# float_info -- a struct sequence with information about the float implementation.
# 包含有关浮点数实现的信息的结构序列

# float_repr_style -- string indicating the style of repr() output for floats
# 指示浮点数的repr()输出样式的字符串

# hash_info -- a struct sequence with information about the hash algorithm.
# hexversion -- version information encoded as a single integer
# implementation -- Python implementation information.
# int_info -- a struct sequence with information about the int implementation.
# maxsize -- the largest supported length of containers.
# maxunicode -- the value of the largest Unicode code point
# platform -- platform identifier
# prefix -- prefix used to find the Python library
# thread_info -- a struct sequence with information about the thread implementation.
# version -- the version of this interpreter as a string
# version_info -- version information as a named tuple
# dllhandle -- [Windows only] integer handle of the Python DLL
# winver -- [Windows only] version number of the Python DLL
# _enablelegacywindowsfsencoding -- [Windows only]

# _clear_type_cache
# 清除内部类型缓存

##################################################################################
# Functions:
#
# displayhook() -- print an object to the screen, and save it in builtins._
# 将一个对象打印到屏幕上并将其保存在build中

# excepthook() -- print an exception and its traceback to sys.stderr
# 打印一个异常及其回溯到sys.stderr

# exc_info() -- return thread-safe information about the current exception
# 返回当前异常的线程安全信息

# exit() -- exit the interpreter by raising SystemExit
# 通过引发SystemExit退出解释器 => sys.exit()

# getdlopenflags() -- returns flags to be used for dlopen() calls
# 返回用于dlopen()调用的标志

# getprofile() -- get the global profiling function
# 获取全局描述函数

# getrefcount() -- return the reference count for an object (plus one :-)
# 返回对象的引用计数

# getrecursionlimit() -- return the max recursion depth for the interpreter
# 返回解释器的最大递归深度 => 999

# getsizeof() -- return the size of an object in bytes
# 以字节为单位返回对象的大小

# gettrace() -- get the global debug tracing function
# 获取全局调试跟踪函数

# setcheckinterval() -- control how often the interpreter checks for events
# 控制解释器检查事件的频率

# setdlopenflags() -- set the flags to be used for dlopen() calls
# 设置用于dlopen()调用的标志

# setprofile() -- set the global profiling function
# 设置全局描述函数

# setrecursionlimit() -- set the max recursion depth for the interpreter
# 设置解释器的最大递归深度

# settrace() -- set the global debug tracing function
# 设置全局调试跟踪函数

##################################################################################
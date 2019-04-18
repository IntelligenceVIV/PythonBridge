# @Time    : 2019/4/18 7:10
# @Author  : Noah
# @File    : multiprocessing_module.py
# @Software: PyCharm
# @description: multiprocessing module
# import multiprocessing as mp
# import os
# import time

# 'Array', 'AuthenticationError', 'Barrier', 'BoundedSemaphore',
# 'BufferTooShort', 'Condition', 'Event', 'JoinableQueue', 'Lock',
# 'Manager', 'Pipe', 'Pool', 'Process', 'ProcessError', 'Queue',
# 'RLock', 'RawArray', 'RawValue', 'SUBDEBUG', 'SUBWARNING',
# 'Semaphore', 'SimpleQueue', 'TimeoutError', 'Value', 'active_children',
# 'allow_connection_pickling', 'context', 'cpu_count', 'current_process',
# 'freeze_support', 'get_all_start_methods', 'get_context', 'get_logger',
# 'get_start_method', 'log_to_stderr', 'process', 'reducer', 'reduction',
# 'set_executable', 'set_forkserver_preload', 'set_start_method', 'sys'

##################################################################################
# Process 类用来描述一个进程对象
# 创建子进程的时候，只需要传入一个执行函数和函数的参数即可完成 Process 示例的创建
# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
#   (1) star() 方法启动进程，
#   (2) join() 方法实现进程间的同步，等待所有进程退出。
#   (3) close() 用来阻止多余的进程涌入进程池 Pool 造成进程阻塞。
#   (4) target 是函数名字，需要调用的函数
#   (5) args 函数需要的参数，以 tuple 的形式传入
# def run_proc(name):
#     print('Child process {0} {1} Running '.format(name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process {0} is Running'.format(os.getpid()))
#     for i in range(5):
#         p = mp.Process(target=run_proc, args=(str(i),))
#         print('process start')
#         p.start()
#     p.join()
#     print('Process close')

##################################################################################
# Pool可以提供指定数量的进程供用户使用 默认是 CPU 核数
# 当有新的请求提交到 Poll 的时候，如果池子没有满时会创建一个进程来执行，否则就会让该请求等待。
# - Pool 对象调用 join 方法会等待所有的子进程执行完毕
# - 调用 join 方法之前，必须调用 close
# - 调用 close 之后就不能继续添加新的 Process

# (1) apply_async 方法用来同步执行进程，允许多个进程同时进入池子
# def run_task(name):
#     print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
#     time.sleep(1)
#     print('Task {0} end.'.format(name))
#
# if __name__ == '__main__':
#     print('current process {0}'.format(os.getpid()))
#     p = mp.Pool(processes=3)
#     for i in range(6):
#         p.apply_async(run_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All processes done!')

##################################################################################
# (2) pool.apply 该方法只能允许一个进程进入池子。在一个进程结束之后，另外一个进程才可以进入池子
# import multiprocessing
# import os
# import time
#
# def run_task(name):
#     print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
#     time.sleep(1)
#     print('Task {0} end.'.format(name))
#
# if __name__ == '__main__':
#     print('current process {0}'.format(os.getpid()))
#     p = multiprocessing.Pool(processes=3)
#     for i in range(6):
#         p.apply(run_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All processes done!')

##################################################################################
# (3) Queue 用来在多个进程间通信。Queue 有两个方法，get 和 put
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码:
# def proc_write(q, urls):
#     print('Process(%s) is writing...' % os.getpid())
#     for url in urls:
#         q.put(url)
#         print('Put %s to queue...' % url)
#         time.sleep(random.random())
#
#
# # 读数据进程执行的代码:
# def proc_read(q):
#     print('Process(%s) is reading...' % os.getpid())
#     while True:
#         url = q.get(True)
#         print('Get %s from queue.' % url)
#
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     proc_writer1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
#     proc_writer2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
#     proc_reader = Process(target=proc_read, args=(q,))
#     # 启动子进程proc_writer，写入:
#     proc_writer1.start()
#     proc_writer2.start()
#     # 启动子进程proc_reader，读取:
#     proc_reader.start()
#     # 等待proc_writer结束:
#     proc_writer1.join()
#     proc_writer2.join()
#     # proc_reader进程里是死循环，无法等待其结束，只能强行终止:
#     proc_reader.terminate()

##################################################################################
# (4) Pipe 进程间通信 (常用来在两个进程间通信，两个进程分别位于管道的两端)
# from multiprocessing import Process, Pipe
#
# def send(pipe):
#     pipe.send(['spam'] + [42, 'egg'])   # send 传输一个列表
#     pipe.close()
#
# if __name__ == '__main__':
#     (con1, con2) = Pipe()                            # 创建两个 Pipe 实例
#     sender = Process(target=send, args=(con1, ))     # 函数的参数，args 一定是实例化之后的 Pip 变量，不能直接写 args=(Pip(),)
#     sender.start()                                   # Process 类启动进程
#     print("con2 got: %s" % con2.recv())              # 管道的另一端 con2 从send收到消息
#     con2.close()                                     # 关闭管道

##################################################################################
# from multiprocessing import Process, Pipe
#
# def talk(pipe):
#     pipe.send(dict(name='Bob', spam=42))            # 传输一个字典
#     reply = pipe.recv()                             # 接收传输的数据
#     print('talker got:', reply)
#
# if __name__ == '__main__':
#     (parentEnd, childEnd) = Pipe()                  # 创建两个 Pipe() 实例，也可以改成 conf1， conf2
#     child = Process(target=talk, args=(childEnd,))  # 创建一个 Process 进程，名称为 child
#     child.start()                                   # 启动进程
#     print('parent got:', parentEnd.recv())          # parentEnd 是一个 Pip() 管道，可以接收 child Process 进程传输的数据
#     parentEnd.send({x * 2 for x in 'spam'})         # parentEnd 是一个 Pip() 管道，可以使用 send 方法来传输数据
#     child.join()                                    # 传输的数据被 talk 函数内的 pip 管道接收，并赋值给 reply
#     print('parent exit')

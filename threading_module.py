# @Time    : 2019/4/18 7:10
# @Author  : Noah
# @File    : threading_module.py
# @Software: PyCharm
# @description: threading module
import threading
import time


# 'Barrier', 'BoundedSemaphore', 'BrokenBarrierError', 'Condition',
# 'Event', 'Lock', 'RLock', 'Semaphore', 'TIMEOUT_MAX', 'Thread',
# 'ThreadError', 'Timer', 'WeakSet', 'activeCount', 'active_count',
# 'currentThread', 'current_thread', 'enumerate', 'get_ident', 'local',
# 'main_thread', 'setprofile', 'settrace', 'stack_size'

# def function(arg):
#     time.sleep(1)
#     print("The function {arg} is running.".format_map({'arg': arg}))
#
#
# if __name__ == "__main__":
#
#     for i in range(5):
#         t = threading.Thread(target=function, args=(i,))
#         t.start()

###########################################################################
# Lock and RLock
# 需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间

# balance = 0
# lock = threading.Lock()
#
#
# def change_balance(n):
#     # 先存后取，结果应该为0
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(10000):
#         # 先要获取锁
#         lock.acquire()
#         try:
#             # 放心地操作
#             change_balance(n)
#         finally:
#             # 改完了一定要释放锁
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

###########################################################################
# RLock允许在同一线程中被多次acquire而Lock却不允许这种情况
# 注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire
# 必须调用n次的release才能真正释放所占用的琐

# lock = threading.Lock()
# # Lock对象
# lock.acquire()
# lock.acquire()
# # 产生了死琐
# lock.release()
# lock.release()

# rLock = threading.RLock()
# # RLock对象
# rLock.acquire()
# rLock.acquire()
# # 在同一线程内，程序不会堵塞
# rLock.release()
# rLock.release()

###########################################################################
# 可以把 Condition 理解为一把高级的琐能够控制复杂的线程同步问题
# def Seeker(cond, name):
#     time.sleep(2)
#     cond.acquire()
#     print('%s :我已经把眼睛蒙上了！'% name)
#     cond.notify()
#     cond.wait()
#     for i in range(3):
#         print('%s is finding!!!'% name)
#         time.sleep(2)
#     cond.notify()
#     cond.release()
#     print('%s :我赢了！'% name)
#
# def Hider(cond, name):
#     cond.acquire()
#     cond.wait()
#     for i in range(2):
#         print('%s is hiding!!!'% name)
#         time.sleep(3)
#     print('%s :我已经藏好了，你快来找我吧！'% name)
#     cond.notify()
#     cond.wait()
#     cond.release()
#     print('%s :被你找到了，唉~^~!'% name)
#
#
# if __name__ == '__main__':
#     cond = threading.Condition()
#     seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
#     hider = threading.Thread(target=Hider, args=(cond, 'hider'))
#     seeker.start()
#     hider.start()

###########################################################################
#  Semaphore在内部管理着一个计数器
#  调用 acquire() 会使这个计数器 -1，release() 则是+1(可以多次release()
#  所以计数器的值理论上可以无限.计数器的值永远不会小于 0
#  当计数器到 0 时，再调用 acquire() 就会阻塞，直到其他线程来调用release()
# num = 0
#
#
# def run(n):
#     # 获得信号量，信号量 -1
#     semaphore.acquire()
#     time.sleep(1)
#     print("run the thread: %s" % n)
#
#     # 释放信号量，信号量 +1
#     semaphore.release()
#
#
# if __name__ == '__main__':
#     # 最多允许2个线程同时运行(即计数器值)
#     # 在多次释放信号量后，计数器值增加后每次可以运行的线程数也会增加
#     semaphore = threading.Semaphore(2)
#     for i in range(20):
#         t = threading.Thread(target=run, args=(i,))
#         t.start()
#
# while threading.active_count() != 1:
#     pass # print(threading.active_count())
# else:
#     print('----all threads done---')
#     print(num)

###########################################################################
# 事件处理的机制：全局定义了一个“Flag”
# 如果“Flag”值为 False 那么当程序执行 event.wait 方法时就会阻塞
# 如果“Flag”值为True 那么执行event.wait 方法时便不再阻塞
# import random
#
#
# def light():
#     # 初始化 event 的 flag 为真
#     if not event.isSet():
#         event.set()  # wait就不阻塞 绿灯状态
#     count = 0
#     while True:
#         if count < 10:
#             print('\033[42;1m---green light on---\033[0m')
#         elif count < 13:
#             print('\033[43;1m---yellow light on---\033[0m')
#         elif count < 20:
#             if event.isSet():
#                 event.clear()
#             print('\033[41;1m---red light on---\033[0m')
#         else:
#             count = 0
#             event.set()  # 打开绿灯
#         time.sleep(1)
#         count += 1
#
#
# def car(n):
#     while 1:
#         time.sleep(random.randrange(3, 10))
#         if event.isSet():
#             print("car [%s] is running..." % n)
#         else:
#             print('car [%s] is waiting for the red light...' % n)
#             # 红灯状态下调用wait方法阻塞，汽车等待状态
#             event.wait()
#
#
# if __name__ == '__main__':
#     car_list = ['BMW', 'AUDI', 'SANTANA']
#     event = threading.Event()
#     Light = threading.Thread(target=light)
#     Light.start()
#     for i in car_list:
#         t = threading.Thread(target=car, args=(i,))
#         t.start()


###########################################################################
# 返回当前存活的线程对象的数量；通过计算len(threading.enumerate())长度而来
# def run():
#     thread = threading.current_thread()
#     print('%s is running...' % thread.getName())  # 返回线程名称
#     time.sleep(10)  # 休眠10S方便统计存活线程数量
#
#
# if __name__ == '__main__':
#     # print('The current number of threads is: %s' % threading.active_count())
#     for i in range(10):
#         print('The current number of threads is: %s' % threading.active_count())  # 返回当前存活线程数量
#         thread_alive = threading.Thread(target=run, name='Thread-***%s***' % i)
#         thread_alive.start()
#
#     # thread_alive.join()
#     print('\n%s thread is done...' % threading.current_thread().getName())

###########################################################################
# threading.current_thread() 返回当前线程对象

# def run(n):
#     thread = threading.current_thread()
#     thread.setName('Thread-***%s***' % n)  # 自定义线程名称
#     print('-' * 30)
#     print("Pid is :%s" % thread.ident)  # 返回线程pid
#     # print('ThreadName is :%s' % thread.name)  # 返回线程名称
#     print('ThreadName is :%s' % thread.getName())  # 返回线程名称
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     # print('The current number of threads is: %s' % threading.active_count())
#     for i in range(3):
#         # print('The current number of threads is: %s' % threading.active_count())    #返回当前存活线程数量
#         thread_alive = threading.Thread(target=run, args=(i,))
#         thread_alive.start()
#     # thread_alive.join()
#     print('\n%s thread is done...' % threading.current_thread().getName())

###########################################################################
# threading.enumerate() 返回当前存在的所有线程对象的列表
# def run(n):
#     thread = threading.current_thread()
#     thread.setName('Thread-***%s***' % n)
#     print('-' * 30)
#     print("Pid is :%s" % thread.ident)  # 返回线程pid
#     # print('ThreadName is :%s' % thread.name)  # 返回线程名称
#     print('ThreadName is :%s' % threading.enumerate())  # 返回所有线程对象列表
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     # print('The current number of threads is: %s' % threading.active_count())
#     threading.main_thread().setName('Noah---python')
#     for i in range(3):
#         # print('The current number of threads is: %s' % threading.active_count())    #返回当前存活线程数量
#         thread_alive = threading.Thread(target=run, args=(i,))
#         thread_alive.start()
#     # thread_alive.join()
#     print('\n%s thread is done...' % threading.current_thread().getName())

###########################################################################
# threading.get_ident() 返回线程pid
# def run(n):
#     print('-'*30)
#     print("Pid is :%s" % threading.get_ident())  # 返回线程pid
#
# if __name__ == '__main__':
#     threading.main_thread().setName('Noah---python')    #自定义线程名
#     for i in range(3):
#         thread_alive = threading.Thread(target=run, args=(i,))
#         thread_alive.start()
#     # thread_alive.join()
#     print('\n%s thread is done...'% threading.current_thread().getName())    #获取线程名

###########################################################################
# threading.main_thread() 返回主线程对象
# 类似 threading.current_thread() 只不过一个是返回当前线程对象，一个是返回主线程对象
# def run(n):
#     print('-' * 30)
#     print("Now Pid is :%s" % threading.current_thread().ident)  # 返回当前线程pid
#     print("Main Pid is :%s" % threading.main_thread().ident)  # 返回主线程pid
#     print('Now thread is %s...' % threading.current_thread().getName())  # 获取当前线程名
#     print('Main thread is %s...' % threading.main_thread().getName())  # 获取主线程线程名
#
#
# if __name__ == '__main__':
#     threading.main_thread().setName('Noah---python')  # 自定义线程名
#     for i in range(3):
#         thread_alive = threading.Thread(target=run, args=(i,))
#         thread_alive.start()
#         time.sleep(2)
#     thread_alive.join()

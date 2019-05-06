# @Time    : 2019/4/28 14:54
# @Author  : Noah
# @File    : aiohttpDemo.py
# @Software: PyCharm
# @description: 是基于asyncio实现的HTTP框架

# 如果把asyncio用在服务器端，例如Web服务器由于HTTP连接就是IO操作
# 因此可以用单线程+coroutine实现多用户的高并发支持

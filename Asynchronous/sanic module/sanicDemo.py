# @Time    : 2019/4/26 15:57
# @Author  : Noah
# @File    : sanicDemo.py
# @Software: PyCharm
# @description: 
from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

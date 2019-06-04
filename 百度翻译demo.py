import http.client
from hashlib import md5
from urllib.parse import quote
import random
import json

# 百度翻译账号
appid = ''
secretKey = ''

 
httpClient = None
myurl = '/api/trans/vip/translate'

# 请求翻译的字段
q = input('please input the keyword: ')
# 翻译源语言
fromLang = 'auto'
# 译文语言
toLang = 'zh'
# 随机数
salt = random.randint(32768, 65536)
# 签名
sign = appid+q+str(salt)+secretKey
m1 = md5()
sign = sign.encode(encoding='utf-8')
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+\
        '&sign='+sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    # 返回结果是json格式
    result = response.read().decode(encoding='utf-8')
    result = json.loads(result)
    print(result['trans_result'][0]['dst'])
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()

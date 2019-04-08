from urllib import request
from urllib import parse # 处理POST数据
import urllib


# 采用get请求
response = request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read().decode('utf-8'))

# 采用POST请求，需要传送数据
data = bytes(parse.urlencode({'word':'hello'}), encoding='utf-8')
response2 = request.urlopen('http://httpbin.org/post', data=data)
print(response2.read())


# 在请求的时候最好设置timeout参数，否则如果一旦超时，程序将会卡死
import socket
try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout): # 这里如果超时，是套接字层面的超时
        print('TIME OUT')

from urllib import request
from urllib import parse

# 采用POST请求的方式模拟请求

URL = "http://httpbin.org/post"

# 利用headers伪装http头部模拟浏览器请求
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Referer' : 'http://202.206.1.163/logout.do'
}


dict_content = {
    'name' : 'value'
}

data = bytes(parse.urlencode(dict_content), encoding='utf-8')
req = request.Request(url=URL, data=data, headers=headers, method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))



import requests

# get请求
url = 'http://httpbin.org/get'
data = {'key':'value'}
# 使用get请求的时候，字典类型的data不用进行处理
response = requests.get(url, data)
print(response.text)

# post请求
url2 = 'http://httpbin.org/post'
data = {'key':'value'}
response = requests.post(url2, data=data)
print(response.text)
print(response.json()) # 把文本进行二次转换转换成返回类型为json格式
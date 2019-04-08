from urllib import request
url = 'http://www.baidu.com'  #前面的http告诉爬虫模块采用http协议
response = request.urlopen(url, timeout=1)  #设置一个超时时间，如果超过1秒没有打开就放弃打开这个网页


#采用read读取的时候会1个字符1个字符读取，而网页采用utf-8协议，1个汉字占用3个字符
print(response.read().decode('utf-8'))  

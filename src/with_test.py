class WithTest():
    def __enter__(self):
        print('run')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None: #如果没有异常，exc_tb的值为None
            print('正常结束')
        else: # 产生异常
            print('has error %s' % exc_tb)
        print('exit')

with WithTest(): # 对类通过with语句进行调用
    print("Test is running")
    raise NameError('test NameError') #手动抛异常 
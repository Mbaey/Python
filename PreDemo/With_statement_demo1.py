class A(object):
    def __enter__(self):
        print('__enter__() called')
        return self

    def print_hello(self):
        print("hello world!")

    def __exit__(self, e_t, e_v, t_b):
        print('__exit__() called')


# 首先会执行__enter__方法
with A() as a:  # a为__enter__的返回对象
    a.print_hello()
    print('got instance')
    # 结束会执行__exit__方法
# http://www.cnblogs.com/chenny7/p/4213447.html
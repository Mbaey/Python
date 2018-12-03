#!D:/LI/Python/Spider
#!/usr/bin/python
import sys
import time
if __name__  == "__main__":
    if(len(sys.argv) >1):
        print("hello： "+ sys.argv[0])
    print(time.time())
    print("Hello World")
    print(len(sys.argv) )
    print(sys.argv[0])

    # for i in range(1, 100):
    #     print('category.dangdang.com/pg' + str(i) + '-cp01.05.16.00.00.00.html')

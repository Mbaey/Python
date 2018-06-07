#
# https://blog.csdn.net/heheyanyanjun/article/details/79199378
def fab(max):
   n, a, b = 0, 0, 1
   while n < max:
      # print b
      yield b
      # print b
      a, b = b, a + b
      n = n + 1
print(fab(5))  # 输出：<generator object fab at 0x00000000069D8A68>
for  n in fab(5):
    print (i, n)    # 依次1,1,2,3,5
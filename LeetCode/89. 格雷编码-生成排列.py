import copy
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        a = [i for i in range(2**n)]
        global_res = []
        global_flag = False
        # print(a)
        def check(a, b):# 1,2,4,8
            diff = abs(a-b)
            while diff % 2 == 0:
                diff /= 2
            return diff==0 or diff==1

        def gen(res, a):
            
            if len(a) == 0:
                if check(res[0], res[-1]):
                    global_res.append(res)
                    global_flag = True
                    #内部函数引用同名变量，并且修改这个变量。python会认为它是局部变量。
                    return True

            for i in a:
                if check(res[-1], i):
                    # res.append(i)
                    res_ = copy.deepcopy(res)
                    a_ = copy.deepcopy(a)

                    res_.append(i)
                    a_.remove(i)

                    if gen(res_, a_):
                        return True

                    # if len(global_res)>0:
                    # global global_flag
                    # if global_flag:
                        # break
        
        a.remove(0)
        gen([0], a)
        
        # print(global_res)
        # for i in global_res[0]:
        #     print(bin(i)) 
        return global_res[0]

if __name__ == "__main__":

    solution = Solution()
    print(solution.grayCode(3))

# 感觉没错啊。
# [[0, 1, 2, 3, 5, 7, 6, 4]]
# 0b0
# 0b1
# 0b10
# 0b11
# 0b101
# 0b111
# 0b110
# 0b100

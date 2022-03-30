import copy
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        a = [0,1]
        for i in range(n-1):
            a_ = copy.deepcopy(a)
            length = len(a_)
            a_ = [a_[length-i-1] + length for i in range(length)]
            a += a_

        return a
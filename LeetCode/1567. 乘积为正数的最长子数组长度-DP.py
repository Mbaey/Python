class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res=0
        iposi, inega = 0, 0
        for i in nums:
            if i < 0:
                iposi, inega = inega, iposi

            if i == 0:
                iposi, inega = 0, 0
            elif i > 0:
                iposi += 1
                inega = (inega + 1 if inega > 0 else 0)
            
            else:
                inega += 1
                iposi = (iposi + 1 if iposi > 0 else 0)
            
            # print(iposi, inega)
            res = max(iposi, res)
            # print(res, imax, imin)
        return res
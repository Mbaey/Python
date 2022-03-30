import bisect
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        val = []
        n1, n2 = len(nums1), len(nums2)
        
        i,j=0,0
        for i, a1 in enumerate(nums1):
            for j, a2 in enumerate(nums2):
                idx = bisect.bisect_left(val, a1+a2)
                if idx >= k: # i,j 元素之和 大于队尾，则之后的j都不符合，之间break
                    break
                if len(val) >= k: # 维护队尾的值足够小，保证上一步，跳过的足够多
                    val.pop()
                    res.pop()
                
                val.insert(idx, a1+a2)
                res.insert(idx, [a1 , a2])
        
        # print(res)
        return res[:k]
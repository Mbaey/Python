class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        找最长的环。 直到找不到。
        0,1,0,0,0
        0,0,1,0,0
        1,0,0,0,0
        0,0,0,0,0
        0,0,0,0,0

        好家伙，二进制枚举法就可以了。
        """
        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/solution/zui-duo-ke-da-cheng-de-huan-lou-qing-qiu-ae0e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def lastRemaining(self, n: int) -> int:
        a1, an = 1, n
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0:  # 正向
                a1 += step
                if cnt % 2:
                    an -= step
            else:  # 反向
                if cnt % 2:
                    a1 += step
                an -= step
            k += 1
            cnt >>= 1
            step <<= 1
        return a1

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/elimination-game/solution/xiao-chu-you-xi-by-leetcode-solution-ydpb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{numerator}/{denominator}" for denominator in range(2, n + 1) for numerator in range(1, denominator) if gcd(denominator, numerator) == 1]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/simplified-fractions/solution/zui-jian-fen-shu-by-leetcode-solution-98zy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
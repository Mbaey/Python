from typing import List
import numpy as np
from bisect import bisect_right


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - \
                house if j < len(heaters) else float('inf')
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans


if __name__ == "__main__":

    solution = Solution()
    # 270
    print(solution.findRadius(
        [2, 5],
        [2]
    )
    )
    # print(solution.visiblePoints(
    #     points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))

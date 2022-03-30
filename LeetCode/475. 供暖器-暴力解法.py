from typing import List
import numpy as np


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res_max = 0
        heaters = np.array(heaters)
        for house in houses:

            heaters_tmp = heaters - house
            length = np.abs(heaters_tmp).min()
            min_radius = length
            # min_radius = 1e9
            # for heat in heaters:
            #     length = abs(heat-house)
            #     if  length < min_radius:
            #         min_radius = length
            #     # 已经存在近距离的加热器了。后面不在寻找
            #     if min_radius < res_max :
            #         break

            if min_radius > res_max:
                res_max = min_radius

        return int(res_max)


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

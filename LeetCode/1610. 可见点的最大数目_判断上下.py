from typing import List

import numpy as np

import numpy as np


class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        x0, y0 = location
        new_points = []
        for point in points:
            new_points.append([point[0]-x0, point[1]-y0])

        def angle_2_radian(angle):  # 360 == 2 pi
            return angle * np.pi / 180

        def get_two_line(toward_angle):
            low_radian = angle_2_radian(toward_angle + angle/2)
            high_radian = angle_2_radian(toward_angle - angle/2)
            # print(toward_angle + angle/2, toward_angle - angle/2)
            # print(low_radian , high_radian)
            if np.abs(low_radian - np.pi / 2) < 1e-6 or np.abs(low_radian + np.pi) / 2 < 1e-6:
                high_k = 0
            else:
                high_k = np.tan(low_radian)
                # low_b = y0 - high_k * x0

            def high_line(x): return high_k * x

            if np.abs(high_radian - np.pi / 2) < 1e-6 or np.abs(high_radian + np.pi / 2) < 1e-6:
                low_k = 0
            else:
                low_k = np.tan(high_radian)
                # high_b = y0 - low_k * x0

            def low_line(x): return low_k * x
            print("high_k, low_k", high_k, low_k)
            # return high_line, low_line
            return high_k, low_k

        def get_point(toward_angle):
            high_line, low_line = get_two_line(toward_angle)

            num = 0
            for point in new_points:
                xt, yt = point
                flag1 = False
                flag2 = False
                diff1 = yt-low_line * xt
                diff2 = yt-high_line * xt
                if low_line < 1e-6:
                    if diff1 >= 1e-6:
                        flag1 = True
                else:
                    if diff1 <= 1e-6:
                        flag1 = True

                if high_line < 1e-6:
                    if diff2 >= 1e-6:
                        flag2 = True
                else:
                    if diff2 <= 1e-6:
                        flag2 = True
                        
                if flag1 and flag2:
                    num += 1

            return num

        max_num = 0
        for toward_angle in range(0, 360, angle):
            num = get_point(toward_angle)
            print(toward_angle, num)
            if num > max_num:
                max_num = num
        return max_num


if __name__ == "__main__":

    solution = Solution()

    print(solution.visiblePoints(
        points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))
    # print(solution.isSelfCrossing([2, 1, 1, 2]))

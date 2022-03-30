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
        location = np.array(location)
        points = np.array(points)
        points -= location

        print(points)

        def angle_2_radian(angle):  # 360 == 2 pi
            return angle * np.pi / 180

        max_num = 0

        linear_transformation_matrix = np.zeros((2, 2))
        for toward_angle in range(0, 360, angle//2):
            # num = get_point(toward_angle)
            low_radian = angle_2_radian(toward_angle - angle/2 - 0)
            high_radian = angle_2_radian((toward_angle + angle/2))

            linear_transformation_matrix[0] = np.cos(
                low_radian), np.sin(low_radian)
            linear_transformation_matrix[1] = np.sin(
                high_radian), np.cos(high_radian)

            linear_transformation_matrix = linear_transformation_matrix.T
            # print(linear_transformation_matrix)
            # new_points = points @ linear_transformation_matrix
            new_points = np.matmul(points, linear_transformation_matrix)

            print("==========")
            print(new_points)
            num = 0
            for point in new_points:
                xt, yt = point
                if xt >= 0 and yt >= 0:
                    num += 1

            print(toward_angle, num)
            if num > max_num:
                max_num = num
            # break
        return max_num


if __name__ == "__main__":

    solution = Solution()
    # 270
    print(solution.visiblePoints(
        points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))
    # print(solution.visiblePoints(
    #     points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))

    # print(solution.isSelfCrossing([2, 1, 1, 2]))

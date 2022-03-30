from bisect import bisect_right
from numpy import arctan2, pi

# 极角转换时，已知两点的坐标可以通过反三角函数来进行转换，一般可以通过反余弦 \texttt{acos}acos，反正弦 \texttt{asin}asin，反正切 \texttt{atan}atan 等函数来确定，但以上函数的返回值范围最多只能覆盖 \piπ，可以利用函数 \texttt{atan2}atan2，不同的语言实现可以参考不同语言的标准库函数。以 \texttt{C++}C++ 为例，「\texttt{atan2}atan2」的返回值范围为 [-\pi,\pi][−π,π]，它的覆盖范围为 2\pi2π。
# ps：我想到二分了。也想到用location做原点。后来想偏了，想着线性变换，求新坐标系下的坐标。如果都是正的，就说明在视线内。
class Solution:
    def visiblePoints(self, points, angle, location):
        sameCnt = 0
        polarDegrees = []
        for p in points:
            if p == location:
                sameCnt += 1
            else:
                polarDegrees.append(
                    arctan2(p[1] - location[1], p[0] - location[0]))
        polarDegrees.sort()

        n = len(polarDegrees)
        polarDegrees += [deg + 2 * pi for deg in polarDegrees]

        degree = angle * pi / 180
        maxCnt = max((bisect_right(
            polarDegrees, polarDegrees[i] + degree) - i for i in range(n)), default=0)

        return maxCnt + sameCnt


if __name__ == "__main__":

    solution = Solution()
    # 270
    print(solution.visiblePoints(
        points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1]))
    # print(solution.visiblePoints(
    #     points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))

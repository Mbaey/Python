import collections
import numpy as np
class DetectSquares:

    def __init__(self):
        self.x2p = collections.defaultdict(list)
        self.y2p = collections.defaultdict(list)

        self.cnt = np.zeros((3005,3005))

    def add(self, point: List[int]) -> None:
        x,y = point
        self.x2p[x].append(point)
        self.y2p[y].append(point)
        self.cnt[x][y] += 1
    def count(self, point: List[int]) -> int:
        x,y = point
        
        xps = self.x2p[x]
        # yps = self.y2p[y]
        # print(self.x2p, xps)
        # print(self.y2p, yps)
        if xps :
            res = 0

            for i in xps: # 对于所有同一个X轴的

                x2, y2 = i
                if x2 == x and y2 == y:
                    break
                    
                length = abs(y2 - y)
                x3 = x + length
                x3_2 = x - length


                res += int(self.cnt[x3][y2]) * int(self.cnt[x3][y])
                if x3_2 < 3005 and x3_2 >=0:
                    res += int(self.cnt[x3_2][y2]) * int(self.cnt[x3_2][y])
            return res
        else:
            return 0

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
import collections
import numpy as np
class DetectSquares:

    def __init__(self):
        self.x2p = collections.defaultdict(list)
        self.y2p = collections.defaultdict(list)

        self.cnt = np.zeros((1005,1005))

    def add(self, point: List[int]) -> None:
        x,y = point
        self.x2p[x].append(point)
        self.y2p[y].append(point)
        self.cnt[x][y] += 1
    def count(self, point: List[int]) -> int:
        x,y = point
        
        xps = self.x2p[x]
        yps = self.y2p[y]
        # print(self.x2p, xps)
        # print(self.y2p, yps)
        if xps and yps:
            res = 0

            for i in xps:
                yy = i[1]
                length = abs(yy - y)
                for j in yps:
                    xx = j[0]
                    len2 = abs(xx - x)
                    if len2 == length: 
                        if xx in self.x2p and yy in self.y2p:
                            res += int(self.cnt[xx][yy])
            return res
        else:
            return 0

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
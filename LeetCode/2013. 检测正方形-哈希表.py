class DetectSquares:

    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.map[y][x] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        if not y in self.map:
            return 0
        yCnt = self.map[y]

        for col, colCnt in self.map.items():
            if col != y:
                # 根据对称性，这里可以不用取绝对值
                d = col - y
                res += colCnt[x] * yCnt[x + d] * colCnt[x + d]
                res += colCnt[x] * yCnt[x - d] * colCnt[x - d]
        
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/detect-squares/solution/jian-ce-zheng-fang-xing-by-leetcode-solu-vwzs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
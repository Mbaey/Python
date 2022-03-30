from collections import deque
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        BLOCKED: 在包围圈中
        VALID:   不在包围圈中
        FOUND:   无论在不在包围圈中，但在 n(n-1)/2 步搜索的过程中经过了 target
        """
        BLOCKED, VALID, FOUND = -1, 0, 1
        BOUNDARY = 10**6

        if len(blocked) < 2:
            return True

        hash_blocked = set(tuple(pos) for pos in blocked)

        def check(start: List[int], finish: List[int]) -> int:
            sx, sy = start
            fx, fy = finish
            countdown = len(blocked) * (len(blocked) - 1) // 2
            
            q = deque([(sx, sy)])
            visited = set([(sx, sy)])
            
            while q and countdown > 0:
                x, y = q.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < BOUNDARY and 0 <= ny < BOUNDARY and (nx, ny) not in hash_blocked and (nx, ny) not in visited:
                        if (nx, ny) == (fx, fy):
                            return FOUND
                        countdown -= 1
                        q.append((nx, ny))
                        visited.add((nx, ny))
            
            if countdown > 0:
                return BLOCKED
            return VALID

        if (result := check(source, target)) == FOUND:
            return True
        elif result == BLOCKED:
            return False
        else:
            result = check(target, source)
            if result == BLOCKED:
                return False
            return True

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/escape-a-large-maze/solution/tao-chi-da-mi-gong-by-leetcode-solution-qxhz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
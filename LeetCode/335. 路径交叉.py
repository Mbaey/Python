from typing import List

import numpy as np


class Solution:
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        return True


if __name__ == "__main__":

    solution = Solution()

    print(solution.isSelfCrossing([1, 2, 2, 1]))
    print(solution.isSelfCrossing([2, 1, 1, 2]))

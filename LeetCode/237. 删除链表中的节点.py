from typing import List

import numpy as np
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # print("node.val", node.val)
        # print(node.next)


if __name__ == "__main__":

    solution = Solution()

    # res = solution.deleteNode(-123)


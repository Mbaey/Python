# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import bisect


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        dummy = ListNode(0, None)
        n = len(lists)
        res = []
        if n == 0:
            return None
        for head in lists:
            node = head
            while node:
                val = node.val
                node = node.next
                bisect.insort_left(res, val)

        # print(res)
        pre = dummy
        for i in res:
            node = ListNode(i, None)
            pre.next = node
            pre = node

        return dummy.next

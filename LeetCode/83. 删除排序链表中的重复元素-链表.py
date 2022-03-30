# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = set()
        it = head
        l = []
        while it:
            val = it.val
            it = it.next

            if val not in s:
                s.add(val)
                l.append(val)

        if not l:
            return None

        res = ListNode()
        pre = res
        for i in l:
            node = ListNode(i, None)
            pre.next = node
            pre = node
        return res.next

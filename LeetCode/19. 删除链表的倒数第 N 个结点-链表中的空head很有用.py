# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        length = 0
        l = []
        while node:
            l.append(node)
            node = node.next
            length += 1
        # print(length)

        if length == n:
            return head.next
        elif n == 1:
            l[length-n-1].next = None
        else:
            l[length-n-1].next = l[length-n+1]

        return head

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         def getLength(head: ListNode) -> int:
#             length = 0
#             while head:
#                 length += 1
#                 head = head.next
#             return length
        
#         dummy = ListNode(0, head)
#         length = getLength(head)
#         cur = dummy
#         for i in range(1, length - n + 1):
#             cur = cur.next
#         cur.next = cur.next.next
#         return dummy.next

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getValue(l1: ListNode) -> int:
            if l1 == None:
                return 0
            else:
                return l1.val
        res = []
        next = 0
        while l1 != None or l2 != None:
            a = getValue(l1)
            if l1 != None:
                l1 = l1.next

            b = getValue(l2)
            if l2 != None:
                l2 = l2.next

            now = a+b+next
            next = now // 10
            now = now % 10
            res.append(now)
            # print(a)
            # print(b)

        if next != 0:
            res.append(next)

        res.reverse()

        nextNode = None
        for i in res:
            nextNode = ListNode(i, next=nextNode)

        return nextNode


if __name__ == "__main__":
    solution = Solution()
    # print("@main")

    l2 = ListNode(3, None)
    l1 = ListNode(4, l2)
    l0 = ListNode(2, l1)
    l0 = ListNode(0, None)

    l22 = ListNode(4, None)
    l11 = ListNode(6, l22)
    l00 = ListNode(5, l11)
    l00 = ListNode(0, None)
    # print(l0.val)
    # l2 = [1,2,3]
    # l2.reverse()
    # print(l2)

    solution.addTwoNumbers(l0, l00)

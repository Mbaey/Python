# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# print(res,type(res))
# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}} <class 'precompiled.listnode.ListNode'>
# 如果解开注释，就变成了。。就会报错。。<__main__.ListNode object at 0x7f9f8d40e0d0> is not valid value for the expected return type ListNode
# <__main__.ListNode object at 0x7f9f8d40e0d0> <class '__main__.ListNode'>


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        it = head
        res = None
        flag = True

        while it:
            # pre = head
            # print(it, type(it), it.val)
            new = ListNode(val=it.val,next=None)
            # print(new)
            if it.val != val:
                if flag:
                    res = new
                    flag = False
                else:
                    pre.next = new
                pre = new

            it = it.next
        # print(res,type(res))
        return res
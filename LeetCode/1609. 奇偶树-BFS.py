# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # l = [1,3]
        # l.pop(0)
        # print(l)
        queue = []
        queue.append([root, 0])
        # print(queue)
        # while len(queue) != 0:
        pre = -1
        flag = True
        isEven = True
        while queue:
            node, level = queue.pop(0)
            val = node.val
            
            # print(pre, val)
            if level % 2:#奇数层
                pass
                if val % 2:
                    return False
                
                if not isEven and pre <= val: #  并不是严格递减，
                    return False

                isEven = False
                pre = val
            else: #偶数层
                if val % 2 == 0:#偶数
                    return False
                # print(isEven)
                if isEven and pre >= val:
                    return False

                    
                isEven = True
                pre = val
                pass

            
            lnode = node.left
            rnode = node.right
            
            if lnode != None:
                queue.append([lnode, level + 1])

            if rnode != None:
                queue.append([rnode, level + 1])
            
            # break

        return True
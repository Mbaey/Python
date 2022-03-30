# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        res = []
        level_traversal = []
        # if 
        # print(root)
        root_list = []
        if root:
            root_list.append( (root, 1, 0) ) # node, level, idx
        level_max = 0
        while root_list:
            node, level, idx = root_list.pop(0)
            
            level_max = max(level_max, level)
            # print( node.val, level, idx)

            while len(level_traversal) < idx  :
                level_traversal.append(None)
            level_traversal.append(node.val)

            # if len(res) < level:
            #     res.append([])
            # idx_fromZero = idx -(2**(level-1)-1)
            # while len(res[level-1]) < idx_fromZero:
            #     res[level-1].append(None)
            # res[level-1].append(node.val)

            l = node.left
            r = node.right

            if l :
                root_list.append((l, level+1, 2*idx+1))
            if r :
                root_list.append((r, level+1, 2*idx+2))

        # print(res)
        
        n = 2** level_max - 1
        while len(level_traversal) < n  :
            level_traversal.append(None) 
        # print(level_traversal)
        # n = len(level_traversal) + 1
        # level_max = int(math.log2(n))
        for level in range(level_max+1):
            level += 1

            nums_of_this_level = 2**(level - 1)
            nums_of_all_father_level = 2**(level - 1) - 1

            l,r = nums_of_all_father_level, nums_of_all_father_level + nums_of_all_father_level + 1

            this_level = level_traversal[l:r]
            if len(this_level) > 1:
                # len(this_level)
                for i in range(nums_of_this_level):
                    if this_level[i] != this_level[nums_of_this_level-i-1]:
                        return False
            # print(this_level)

        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        # if 
        # print(root)
        root_list = []
        if root:
            root_list.append( (root, 1) )
        while root_list:
            node, level = root_list.pop(0)
            if len(res) < level:
                res.append([])
            # print(level, node.val, res)

            res[level-1].append(node.val)

            l = node.left
            r = node.right

            if l :
                root_list.append((l, level+1))
            if r :
                root_list.append((r, level+1))

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            res.append(node.val)
            l = node.left
            r = node.right

            if l :
                dfs(l, res)
            if r :
                dfs(r, res)
        
        res = []
        if root:
            dfs(root, res)

        return res
    

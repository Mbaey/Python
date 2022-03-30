
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            if root1 == root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        if not root: return True
        return dfs(root.left, root.right)

# 作者：fe-lucifer
# 链接：https://leetcode-cn.com/problems/symmetric-tree/solution/dfs-shen-ru-qian-chu-101-dui-cheng-er-cha-shu-by-f/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
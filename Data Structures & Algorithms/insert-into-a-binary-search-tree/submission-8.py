class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(root):
            cur = root

            if cur.val < val and cur.right is None:
                cur.right = TreeNode(val)
                return cur

            elif cur.val > val and cur.left is None:
                cur.left = TreeNode(val)
                return cur

            if cur.val < val:
                cur.right = dfs(cur.right)

            elif cur.val > val:
                cur.left = dfs(cur.left)

            return cur

        if not root:
            return TreeNode(val)

        return dfs(root)
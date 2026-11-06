# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return TreeNode(val)

            cur = root

            if cur.val > val and cur.left is None:
                cur.left = TreeNode(val)

            elif cur.val < val and cur.right is None:
                cur.right = TreeNode(val)


            if cur.val < val:
                cur.right = dfs(root.right)

            elif cur.val > val:
                cur.left = dfs(root.left)


            return cur

        return dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        dummy = TreeNode(0)
        dummy.left = root

        def dfs(root , parent):
            if not root:
                return 
            
            dfs(root.left , root)
            dfs(root.right , root)


            if root.left == None and root.right == None and root.val == target:
                if parent.left == root:
                    parent.left = None

                if parent.right == root:
                    parent.right = None

        dfs(root , dummy)

        return dummy.left

        
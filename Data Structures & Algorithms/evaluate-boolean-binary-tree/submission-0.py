# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        



        def dfs(root):
            if root.val == 0:
                return False
            
            elif root.val ==1:
                return True

            elif root.val ==3:
                left = dfs(root.left)
                right = dfs(root.right)
                return left and right

            elif root.val ==2:
                left = dfs(root.left)
                right = dfs(root.right)
                return left or right


        return dfs(root)









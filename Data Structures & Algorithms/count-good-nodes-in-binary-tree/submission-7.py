# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def dfs (root  , maxx):
            nonlocal count 

            if not root:
                return None

            if(root.val >= maxx):
                count  = count + 1
               
            maxx = max(root.val , maxx)
            

            dfs(root.right , maxx)
            dfs(root.left , maxx)


        dfs(root , root.val)
        return count 


            


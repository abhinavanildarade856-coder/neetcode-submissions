# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        reu = []

        def preor(root):
            if not root:
                return

            reu.append(root.val)
            preor(root.left)
            preor(root.right)


        preor(root)
        return reu



            

        
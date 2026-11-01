# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        
        def get_leaves(root):
            leaf = []

            def leafs(root):
                

                if root is None:
                    return 

                if root.left is None and root.right is None:
                    leaf.append(root.val)
                    return 

                leafs(root.left)
                leafs(root.right)

            leafs(root)
            return leaf

        return get_leaves(root1) == get_leaves(root2)






            




        
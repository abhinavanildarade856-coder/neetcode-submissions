# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Create a hash map to store the indices of the inorder values for O(1) lookups
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Turn preorder into an iterator since we process elements strictly in order
        preorder_iter = iter(preorder)
        
        def build_subtree(left_bound, right_bound):
            # Base case: if there are no elements to construct the subtree
            if left_bound > right_bound:
                return None
            
            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find where this root is in the inorder traversal
            mid = inorder_index_map[root_val]
            
            # Recursively build the left and right subtrees.
            # IMPORTANT: We must build the left subtree first because the preorder 
            # iterator provides elements in Root -> Left -> Right order.
            root.left = build_subtree(left_bound, mid - 1)
            root.right = build_subtree(mid + 1, right_bound)
            
            return root
            
        return build_subtree(0, len(inorder) - 1)
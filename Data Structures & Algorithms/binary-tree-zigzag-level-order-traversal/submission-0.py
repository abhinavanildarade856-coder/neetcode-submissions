# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        result = []

        def bt(root):
            if not root:
                return []

            z = 1
            q = deque([root])

            while q:
                n = len(q)
                level = []

                for _ in range(n):
                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

                if z%2 == 0:
                    result.append(reversed(level))
                else:
                    result.append(level)
                z+=1

            
        bt(root)
        return result

        








            


            

        
from collections import deque
from typing import Optional

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        level_sum = []
        q = deque([root])

        # Calculate the sum of each level
        while q:
            cur_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sum.append(cur_sum)

        # Replace each node's value with its cousin sum
        q = deque([(root, 0)])
        root.val = 0
        level = 1

        while q:
            for _ in range(len(q)):
                node, _ = q.popleft()

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val

                if node.left:
                    node.left.val = level_sum[level] - child_sum
                    q.append((node.left, 0))

                if node.right:
                    node.right.val = level_sum[level] - child_sum
                    q.append((node.right, 0))

            level += 1

        return root
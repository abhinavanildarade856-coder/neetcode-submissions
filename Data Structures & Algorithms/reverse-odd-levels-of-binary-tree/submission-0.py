from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        q = deque([root])
        level_num = 0

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append(node)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if level_num % 2 == 1:
                left = 0
                right = len(level) - 1

                while left < right:
                    level[left].val, level[right].val = (
                        level[right].val, level[left].val
                    )
                    left += 1
                    right -= 1

            level_num += 1

        return root
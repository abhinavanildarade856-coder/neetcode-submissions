from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        res = []
        q = deque([root])

        while q:
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_sum)

        res.sort(reverse=True)

        return res[k - 1] if len(res) >= k else -1
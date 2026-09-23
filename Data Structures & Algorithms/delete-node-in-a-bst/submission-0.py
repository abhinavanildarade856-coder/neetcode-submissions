class Solution:
    def deleteNode(self, root, key):

        if not root:
            return None

        curr = root
        parent = None

        # 1. Find the node
        while curr and curr.val != key:
            parent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # Key not found
        if not curr:
            return root

        # 2. Node has TWO children
        if curr.left and curr.right:

            # Find inorder successor
            successor_parent = curr
            successor = curr.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            curr.val = successor.val

            # Now delete the successor
            parent = successor_parent
            curr = successor

        # 3. Node has 0 or 1 child
        if curr.left:
            child = curr.left
        else:
            child = curr.right

        # curr is root
        if parent is None:
            return child

        # Connect parent directly to child
        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child

        return root
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        def help(l , r):
            if l > r:
                return None
            
            m = (l+r) // 2

            root = TreeNode(nums[m])
            root.left = help(l , m - 1)
            root.right = help (m + 1  , r)
            return root


        return help(0 , len(nums)-1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        n  = len(nums)

        sol ,res =[] , []


        def bt(i):

            if i == n:
                res.append(sol[:])
                return 


            bt(i+1)

            sol.append(nums[i])
            bt(i+1)
            sol.pop()

        bt(0)

        return res



        
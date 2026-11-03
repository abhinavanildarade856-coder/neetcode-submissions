class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res, sol = [] , [] 


        def bt(i):
            if i == len(nums):
                if sol not in res:
                    res.append(sol[:])
                return 
            bt(i+1)

            sol.append(nums[i])
            bt(i+1)
            sol.pop()


        bt(0)
        return res

            
        
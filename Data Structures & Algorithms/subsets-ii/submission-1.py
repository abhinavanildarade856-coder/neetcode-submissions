class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol  , res = []  , [] 

        def bt(start):
            res.append(sol[:])

            for i in range(start , len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                sol.append(nums[i])
                bt(i+1)
                sol.pop()

        bt(0)
        return res 
        
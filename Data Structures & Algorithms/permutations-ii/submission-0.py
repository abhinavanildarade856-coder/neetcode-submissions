class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol , res = [] , []
        used = [False] * len(nums)

        def bt(start):
            if len(sol) == len(nums):
                res.append(sol[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue

                used[i] = True
                sol.append(nums[i])
                
                bt(i+1)


                sol.pop()
                used[i] = False

        bt(0)
        return res





        
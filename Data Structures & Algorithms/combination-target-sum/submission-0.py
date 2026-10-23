class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        sol , res = [] , []

        def bt(i):
            summ = sum(sol)

            if summ == target:
                res.append(sol[:])
                return 

            if i ==n  or summ > target:
                return 

            bt(i+1)

            sol.append(nums[i])
            bt(i)
            sol.pop()

        bt(0)
        return res             
                
                

             
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol , res =[] , [] 



        def bt(start):
            sett = set()
            j = 0
            if  len(sol) ==len(nums):
                res.append(sol[:])
                return 

            for i in range(len(nums)):
                if nums[i] in sol:
                    continue
                sol.append(nums[i])
                bt(i+1)
                sol.pop()

 
        
        bt(0)
        return res

            

            
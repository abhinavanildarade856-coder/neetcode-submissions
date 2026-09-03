class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        
        for x in range(len(nums)):
            for j in range(x+1 , len(nums)):
                if nums[x] + nums[j] == target:
                    return [x,j]

                 
        




        
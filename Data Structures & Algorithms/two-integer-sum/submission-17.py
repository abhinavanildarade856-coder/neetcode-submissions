class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for i , n  in enumerate(nums):
            temp = target - n
            if temp in prevmap:
                return [prevmap[temp], i]
            
            prevmap[n] = i

        




        
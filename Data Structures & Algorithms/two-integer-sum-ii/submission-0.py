class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l =0
        r = (len(numbers)-1)

        while r > l :
            temp = nums[l] + nums[r]

            if temp > target:
                r = r-1
            elif temp < target:
                l = l + 1
            elif temp == target:
                return [l+1,r+1]
        
        
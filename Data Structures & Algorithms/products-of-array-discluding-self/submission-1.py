class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mul = []

        for i in range(len(nums)):
            product=1
            for j in  range(len(nums)):
                if j != i:
                    product *= nums[j]
            mul.append(product)
        return mul



  


        

      
            


        
                






             

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ot = []
        
        for i in range(n):
            temp = 1
            for j in range(n):
                if j != i:
                    temp  = temp * nums[j]
            ot.append(temp)
        return ot
                    

                

    


  


        

      
            


        
                






             

        
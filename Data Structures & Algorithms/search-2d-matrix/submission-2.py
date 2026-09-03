class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            
            if matrix[i][0] <= target <= matrix[i][-1]:
                temp = matrix[i]

                l = 0 
                r = len(temp) - 1  

                while l <= r:
                    
                    mid  = (r + l) // 2

                    if target > temp[mid]:
                        l = mid + 1
                    elif target < temp[mid]:
                        r = mid - 1
                    elif target == temp[mid]:
                        return True 
        return False




                


        
        
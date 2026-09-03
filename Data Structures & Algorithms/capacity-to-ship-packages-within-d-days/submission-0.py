class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)
        res = right

        def canship(cap):
            ships , curcap = 1 , cap
            for w in weights:
                if curcap - w < 0:
                    ships +=1
                    curcap = cap
                curcap -=w
            
            return ships <= days

        while left <= right:
            cap =( left +right) // 2

            if canship(cap):
                res = min(res , cap)
                right = cap - 1
            else:
                left = cap +1
        return left
                    






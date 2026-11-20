class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []

        for i  , v  in enumerate(nums):
            count[v]  = count.get(v , 0) + 1

        more =  abs(len(nums)/3)

        for i  , v in count.items():
            if v > more:
                res.append(i)

        return res

        


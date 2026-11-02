class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res , sol  = []  , [] 

        def bt(start):
            if len(sol) == k:
                res.append(sol[:])
                return 

            for i in range(start , n):
                sol.append(i +1)
                bt(i+1)
                sol.pop()

        bt(0)

        return res

        
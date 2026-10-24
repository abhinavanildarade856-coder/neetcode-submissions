class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        n = len(candidates)

        sol , res = [] , []


        def bt(i):
            summ = sum(sol)

            if summ == target:
                res.append(sol[:])
                return

            if i == n or summ > target:
                return

            
            sol.append(candidates[i])
            bt(i+1)
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            bt(i+1)

        bt(0)

        return res

            
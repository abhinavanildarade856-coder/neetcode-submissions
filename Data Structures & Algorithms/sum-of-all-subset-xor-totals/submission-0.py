class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        sol , res = [], 0
        
        def bt(i):
            nonlocal res

            if i ==n:
                x=0
                for i in sol:
                    x ^= i
                res += x
                return 


            bt(i+1)

            sol.append(nums[i])
            bt(i+1)
            sol.pop()


        bt(0)
        return res



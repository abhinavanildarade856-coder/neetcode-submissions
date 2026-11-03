class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(path, choices):
            if not choices:
                result.append(path)
                return
            for i in range(len(choices)):
                backtrack(path + [choices[i]], choices[:i] + choices[i+1:])
                
        backtrack([], nums)
        return result

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0


        for n in setnums:
            length =0
            if (n-1) not in setnums:

                while (n+length) in setnums:
                    length+=1
                    longest = max(longest , length)

        return longest


 



        
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(substring):
            return substring==substring[::-1]

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (check(s[l+1:r+1]) or check(s[l:r]))
            l+=1
            r-=1
        return True
        

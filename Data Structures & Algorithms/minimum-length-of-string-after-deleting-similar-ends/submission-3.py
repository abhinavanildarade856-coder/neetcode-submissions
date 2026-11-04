class Solution:
    def minimumLength(self, s: str) -> int:
        l , r = 0 , len(s)-1

        if len(s) == 1:
            return 1

        while l < r and s[l] == s[r]:
                ch = s[l]

                while l <= r and s[l] ==ch:
                    l+=1
                
                while l<=r and s[r] ==ch:
                    r -=1


        return max( 0 , r - l + 1)


            

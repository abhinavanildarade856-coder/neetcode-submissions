class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     freq_s = {}
     freq_t = {}

     for x in s:
        if x in freq_s:
            freq_s[x] +=1
        else:
            freq_s[x] = 1


     for y in t:
        if y in freq_t:
            freq_t[y] +=1
        else:
            freq_t[y] = 1

     b = (freq_s == freq_t)


     return b





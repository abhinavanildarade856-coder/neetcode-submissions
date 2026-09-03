class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     freq_s = {}
     freq_t = {}
     
     for x in s:
        if x in freq_s:
            freq_s[x] +=1
        else:
            freq_s[x] = 1

     for x in t:
        if x in freq_t:
            freq_t[x] +=1
        else:
            freq_t[x] = 1
            
     b = (freq_s == freq_t)
     return b
    

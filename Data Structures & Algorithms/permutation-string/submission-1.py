class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s2) < len(s1):
            return False

        count = [0]*26
        window = [0]*26



        for ch in s1:
            count[ord(ch) - ord('a')]+=1

            
        for i in range(len(s2)):

            window [ord(s2[i]) - ord('a')] +=1

            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord('a')] -=1

            if count==window:
                return True

        return False



        # if len(s2) < len(s1):
        #     return False

        # count1 = [0]*26
        # window= [0]*26


        # for ch in s1:
        #     count1[ord(ch) - ord('a')] +=1

        
        # for i in range(len(s2)):
        #    window[ord(s2[i]) - ord('a')] +=1


        #    if i >= len(s1):
        #         window[ord (s2 [i - len(s1)] ) - ord('a')] -= 1

        #    if count1==window:
        #         return True

        # return False 




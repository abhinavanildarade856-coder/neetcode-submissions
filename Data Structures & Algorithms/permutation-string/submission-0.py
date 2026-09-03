class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Count characters in s1
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        # Sliding window of size len(s1)
        for i in range(len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1

            # Remove character outside the window
            if i >= len(s1):
                count2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Same character frequencies => permutation exists
            if count1 == count2:
                return True

        return False
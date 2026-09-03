class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        l = []

        for key in list(freq.keys())[:k]:
            l.append(key)

        return l





class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}


        for r in range(len(nums)):
            if nums[r] in seen:
                if r - seen[nums[r]] <=k:
                    return True
            
            seen[nums[r]] = r

        return False

        
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        nums1 = nums[-k:]
        nums2 = nums[:-k]

        nums.clear()

        for i in nums1:
            nums.append(i)

        for j in nums2:
            nums.append(j)
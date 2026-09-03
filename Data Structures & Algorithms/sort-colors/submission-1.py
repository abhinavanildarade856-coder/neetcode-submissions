class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def merge(arr, L, R, M):
            left = arr[L:M+1]
            right = arr[M+1:R+1]

            i = j = 0
            k = L

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        def mergesort(arr, l, r):
            if l >= r:
                return

            m = (l + r) // 2

            mergesort(arr, l, m)
            mergesort(arr, m + 1, r)

            merge(arr, l, r, m)

        mergesort(nums, 0, len(nums) - 1)
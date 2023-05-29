# Given an array of integers nums and an integer k,
# return the number of contiguous subarrays
# where the product of all the elements in the subarray is strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = l = 0
        prod = 1

        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            ans += r - l + 1

        return ans

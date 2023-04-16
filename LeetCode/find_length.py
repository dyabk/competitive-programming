# Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.
class Solution:
    def find_length(nums, k):
        ans = 0
        l = 0

        cur_len = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_len += 1
            cur_sum += nums[r]
            while cur_sum > k:
                cur_sum -= nums[l]
                cur_len -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

# Given an array of integers nums,
# you start with an initial positive value startValue.
# In each iteration,
# you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        return 1 - min(prefix)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curAvg, curSum, maxAvg = 0, 0, float('-inf')
        for i in range(len(nums)):
            curSum += nums[i]
            if i >= k:
                curSum -= nums[i - k]
            if i >= k - 1:
                curAvg = curSum / k
                maxAvg = max(curAvg, maxAvg)

        return maxAvg

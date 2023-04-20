class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        prefix_sums = [0] * N
        prefix_sums[0] = nums[0]
        for i in range(1, N):
            prefix_sums[i] += prefix_sums[i - 1] + nums[i]
        answer = 0
        for i in range(N - 1):
            if prefix_sums[i] >= prefix_sums[N - 1] - prefix_sums[i]:
                answer += 1
        return answer

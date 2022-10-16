class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, flip, curRes, maxRes = 0, 0, 0, 0
        for j in range(len(nums)):
            if nums[j] == 0:
                while flip >= k:
                    if nums[i] == 0:
                        flip -= 1
                    curRes -= 1
                    i += 1
                flip += 1
            curRes += 1
            maxRes = max(maxRes, curRes)

        return maxRes

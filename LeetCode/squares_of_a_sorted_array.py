class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        answer = [0] * len(nums)
        i = len(nums) - 1
        while l <= r and l < len(nums) and r >= 0:
            if abs(nums[l]) > abs(nums[r]):
                answer[i] = nums[l] * nums[l]
                l += 1
            else:
                answer[i] = nums[r] * nums[r]
                r -= 1
            i -= 1

        return answer

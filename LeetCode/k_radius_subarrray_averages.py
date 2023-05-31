class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        answer = []
        
        for i in range(len(nums)):
            l, r = i - k, i + k
            preL = prefix[l - 1] if l > 0 else 0
            if l >= 0 and r < len(nums):
                answer.append((prefix[r] - preL) // (2 * k + 1))
            else:
                answer.append(-1)
            
        return answer
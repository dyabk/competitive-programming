class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        while left < len(s) // 2:
            s[left], s[~left] = s[~left], s[left]
            left += 1

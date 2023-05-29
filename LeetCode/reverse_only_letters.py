class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        l, r = 0, len(s) - 1

        new_str = []

        while l < len(s):
            if not s[l].isalpha():
                new_str.append(s[l])
            else:
                while r > 0 and not s[r].isalpha():
                    r -= 1
                new_str.append(s[r])
                r -= 1
            l += 1
            
        return "".join(new_str)
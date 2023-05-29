# Given a string s,
# reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        
        new_str = []
        
        l, r = 0, 0
        print(len(s))
        while r < len(s) + 1:
            if r == len(s) or s[r] == ' ':
                for i in range(r - 1, l - 1, -1):
                    new_str.append(s[i])
                if r != len(s):
                    new_str.append(s[r])
                l = r = r + 1
            r += 1
        return "".join(new_str)
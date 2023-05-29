class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:         
        
        word_list = list(word)
        l, r = 0, 0
        for i in range(len(word_list)):
            if word_list[i] == ch:
                r = i
                break
        while (l <= r):
            word_list[l], word_list[r] = word_list[r], word_list[l]
            l += 1
            r -= 1
        return "".join(word_list)
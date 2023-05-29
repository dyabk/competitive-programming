class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters = 'aeiou'
        start = 0
        vowel_count = 0
        answer = 0
        for end in range(len(s)):
            if s[end] in vowel_letters:
                vowel_count += 1
            if end - start + 1 == k:
                answer = max(answer, vowel_count)
                if s[start] in vowel_letters:
                    vowel_count -= 1
                start += 1
        return answer
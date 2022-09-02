from collections import Counter


def find_substring(str1, pattern):
    # TODO: Write your code here
    answer = ""

    pc = Counter(pattern)
    m = Counter()
    left = 0

    for right in range(len(str1)):
        m[str1[right]] += 1

        while all(pc[c] <= m[c] for c in pc) and (answer == "" or right - left + 1 <= len(answer)):
            answer = str1[left:right+1]
            print(answer)
            m[str1[left]] -= 1
            left += 1

    return answer

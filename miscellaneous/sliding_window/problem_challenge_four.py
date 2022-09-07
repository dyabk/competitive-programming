from collections import Counter


def find_word_concatenation(str1, words):
    word_count = len(words)
    word_frequency = Counter(words)
    word_length = len(words[0])

    result_indices = []

    for i in range((len(str1) - word_count * word_length) + 1):
        seen_words = Counter()
        for j in range(0, word_count):
            next_word_index = i + j * word_length
            possible_word = str1[next_word_index:next_word_index + word_length]
            if possible_word not in word_frequency:
                break
            seen_words[possible_word] += 1
            if seen_words[possible_word] > word_frequency[possible_word]:
                break
            if j + 1 == word_count:
                result_indices.append(i)

    return result_indices

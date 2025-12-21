from collections import Counter

def is_anagram(input, words_dict):
    for char in input:
        if char not in words_dict.keys():
            return False
        updated_count = words_dict[char] - 1
        if updated_count == 0:
            del words_dict[char]
        else:
            words_dict[char] = updated_count
    return len(words_dict) == 0


def anagram_indexes(original, check):
    window_size = len(check)
    anagram_dict =  Counter(check)
    result = []

    left = 0
    right = left + window_size

    while right < len(original):
        words_dict = anagram_dict.copy()
        if is_anagram(original[left:right], words_dict):
            result.append(left)
        left += 1
        right +=1

    return result

if __name__ == '__main__':
    original = "cbaebabacd"
    check = "abc"
    print(anagram_indexes(original, check))
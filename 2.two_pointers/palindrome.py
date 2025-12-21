def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while not s[left].isalnum():
            left = left + 1
        while not s[right].isalnum():
            right = right - 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))
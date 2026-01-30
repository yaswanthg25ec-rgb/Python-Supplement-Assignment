# Problem 8: Check if a string is palindrome
# Find and fix the error

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

word="racecar"

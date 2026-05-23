class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_string = ""
        for char in s:
            if char.isalnum():
                str_string+=char.lower()
        return str_string == str_string[::-1]
            
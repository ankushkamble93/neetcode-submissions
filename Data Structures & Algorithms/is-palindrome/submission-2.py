class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_str = [char.lower() for char in s if char.isalnum()]
        cleaned_str = "".join(updated_str)
        return cleaned_str == cleaned_str[::-1]

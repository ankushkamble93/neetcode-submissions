class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_strings = "".join(sorted(s))
        sorted_stringt = "".join(sorted(t))
        return sorted_strings == sorted_stringt
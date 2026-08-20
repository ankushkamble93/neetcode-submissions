class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1, lens2 = len(s1), len(s2)
        if lens1 > lens2:
            return False
        counts1 = Counter(s1)
        counts2 = Counter(s2[:lens1])
        if counts1 == counts2:
            return True
        for i in range(lens1, lens2):
            counts2[s2[i]] += 1
            left_char = s2[i-lens1]
            counts2[left_char]-=1
            if counts2[left_char]==0:
                del counts2[left_char]
            if counts1 == counts2:
                return True
        return False
        
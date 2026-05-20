class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sorted_word = "".join(sorted(s))
            if sorted_word in seen:
                seen[sorted_word].append(s)
            else:
                seen[sorted_word] = [s]
        return list(seen.values())

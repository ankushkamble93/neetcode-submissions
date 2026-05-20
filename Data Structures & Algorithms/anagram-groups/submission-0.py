class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            seen_word = "".join(sorted(s))
            if seen_word not in seen:
                seen[seen_word] = []
            seen[seen_word].append(s)
        return list(seen.values())

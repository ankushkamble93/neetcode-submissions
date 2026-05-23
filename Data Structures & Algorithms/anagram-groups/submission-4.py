from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            seen[sorted_str].append(string)
        return list(seen.values())
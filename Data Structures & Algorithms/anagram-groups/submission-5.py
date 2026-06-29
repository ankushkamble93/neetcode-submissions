class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in range(len(strs)):
            sorted_key = "".join(sorted(strs[i]))
            if sorted_key in output:
                output[sorted_key].append(strs[i])
            else:
                output[sorted_key] = [strs[i]]

        return list(output.values())
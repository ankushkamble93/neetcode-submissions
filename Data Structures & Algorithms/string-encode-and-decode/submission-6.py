class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            string += str(len(strs[i])) + "#" + strs[i]
        return string

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            word_start = j + 1
            word_length = int(s[i:j])
            word_end = word_length + word_start
            output.append(s[word_start:word_end])
            i = word_end
        return output


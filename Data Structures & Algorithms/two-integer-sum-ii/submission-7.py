class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            current_num = numbers[i]
            complement = target - current_num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[current_num] = i
                

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_dict = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers_dict:
                return [numbers_dict[diff], i+1]
            numbers_dict[numbers[i]] = i+1
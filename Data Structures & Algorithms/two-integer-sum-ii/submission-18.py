class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)
        while left < right:
            complement = numbers[left] + numbers[right-1]
            if complement == target:
                return [left+1, right]
            elif complement > target:
                right -=1
            elif complement < target:
                left+=1
        return[]

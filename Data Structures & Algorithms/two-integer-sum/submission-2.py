class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            target_num = target - n
            if target_num in seen:
                return list({seen[target_num],i})
            seen.update({n:i})
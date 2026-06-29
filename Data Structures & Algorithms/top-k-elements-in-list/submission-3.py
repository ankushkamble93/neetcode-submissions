class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for i in range(len(nums)):
            if nums[i] in output:
                output[nums[i]] += 1
            else:
                output[nums[i]] = 1
        return sorted(output, key=output.get, reverse=True)[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_list = {}
        for num in nums:
            if num in count_list:
                count_list[num] += 1
            else:
                count_list[num] = 1
        highest_values = sorted(count_list.keys(),key = count_list.get, reverse=True)[:k]
        return highest_values
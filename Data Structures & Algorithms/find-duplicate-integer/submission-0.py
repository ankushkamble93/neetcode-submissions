class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        for num, count in hashmap.items(): 
            if count > 1: return num
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for num in nums_set:
            if (num-1) not in nums_set:
                length = 0
                while (length+num) in nums_set:
                    length+=1
                longest_streak = max(longest_streak, length)
        return longest_streak
                 

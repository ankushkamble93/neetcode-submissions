class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_streak = 0
        for num in numset:
            if (num-1) not in numset:
                current_streak=1
                current_count=num
                while(current_count+1 in numset):
                    current_streak+=1
                    current_count+=1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak

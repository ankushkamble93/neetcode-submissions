class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort() # [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < 0:
                    left+=1
                elif current_sum > 0:
                    right-=1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -=1
        return output
                
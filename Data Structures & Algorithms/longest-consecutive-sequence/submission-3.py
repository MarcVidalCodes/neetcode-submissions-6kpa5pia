class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        longest = 1
        curr_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue 
            elif nums[i] == nums[i-1] + 1: 
                curr_streak +=1 
            else: 
                longest = max(longest, curr_streak)
                curr_streak = 1 
        return max(longest, curr_streak)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums_set = set(nums)
        longest = 1 

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num 
                streak = 1 
            
                while current + 1 in nums_set: 
                    streak += 1
                    current += 1
            
                longest = max(longest, streak)
        return longest
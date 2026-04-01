class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0: 
            return 0
            
        nums_set = set(nums)

        max_consecutive = 1
        for num in nums: 
            consecutive_num = num + 1
            current_consecutive = 1 

            while consecutive_num in nums_set: 
                current_consecutive += 1
                max_consecutive = max(current_consecutive, max_consecutive)
                consecutive_num += 1

        return max_consecutive
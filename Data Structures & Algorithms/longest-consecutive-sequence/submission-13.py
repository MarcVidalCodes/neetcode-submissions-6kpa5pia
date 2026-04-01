class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0 

        for num in nums: 
            seq = 1
            curr = num 
            
            while curr + 1 in nums_set: 
                seq += 1
                curr += 1
            
            res = max(res, seq)
        return res
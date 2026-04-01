class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0: return 0
        res = 1
        nums_set = set()
        for num in nums: 
            nums_set.add(num)

        for num in nums_set: 
            next_num = num + 1
            current_seq = 1 

            while next_num in nums_set:
                current_seq += 1
                res = max(res, current_seq)
                next_num += 1
        return res
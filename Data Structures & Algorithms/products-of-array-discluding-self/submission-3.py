class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        #prefix
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        #suffix
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        #result
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res

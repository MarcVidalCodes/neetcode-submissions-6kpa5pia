class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] *n

        pref[0] = suff[n-1] = 1

        #[1, 1, 2, 8] 
        #[48, 24, 6, 1]
        for i in range(1, len(nums), 1):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for num in range(n): 
            res[num] = pref[num] * suff[num]

        return res

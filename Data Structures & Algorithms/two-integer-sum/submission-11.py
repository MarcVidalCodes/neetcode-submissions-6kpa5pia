class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #number, index

        hm = {}

        for i,x in enumerate(nums):
            diff = target - x

            if diff in hm:
                return [hm[diff], i]
            
            hm[x] = i

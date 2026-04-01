class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {} 
        res = [] 
        #key, value
        #number, freq

        for num in nums: 
            hm[num] = 1 + hm.get(num, 0)

        while k > 0: 
            max_key = max(hm, key = hm.get)
            res.append(max_key)
            hm[max_key] = 0
            k-=1 
        return res
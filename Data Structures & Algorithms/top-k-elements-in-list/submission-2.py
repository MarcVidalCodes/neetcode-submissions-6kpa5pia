class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        #key, value
        #num, cnt 
        res = [] 

        for num in nums: 
            if num not in hm: 
                hm[num] = 1
            else: 
                hm[num] += 1

        for _ in range(k):
            max_key = max(hm, key = hm.get)
            res.append(max_key)
            hm[max_key] = 0
        
        return res 

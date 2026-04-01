class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        res, l, max_f = 0, 0, 0 

        #aabbaaa k = 1
        # l r

        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(count.values())

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)
        return res
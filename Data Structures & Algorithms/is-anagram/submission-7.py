class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_set = {} 
        t_set = {} 
        #key, value
        # letter, freq
        for x in s: 
            s_set[x] = 1 + s_set.get(x, 0)
        
        for x in t: 
            t_set[x] = 1 + t_set.get(x, 0)
        
        return s_set == t_set 
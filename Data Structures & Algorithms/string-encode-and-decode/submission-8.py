class Solution:

    def encode(self, strs: List[str]) -> str:
        #[hello, world]
        #5_hello5_world
        res = ""
        for s in strs: 
            res += str(len(s)) + "_" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = [] 

        i = 0 
        while i < len(s): 
            j = i
            while s[i] != '_': 
                i += 1
            
            count = int(s[j:i])
            j = i + 1
            i = j + count
            res.append(s[j:i])
        return res

            


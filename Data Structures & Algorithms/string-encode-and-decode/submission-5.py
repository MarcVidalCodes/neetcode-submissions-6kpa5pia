class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs: 
            string += str(len(s)) + "_" + s
            #0123456789
            #4_neet4_code_4love_3you
            #  i   j

        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 

        while i < len(s):
            j = i 
            while s[j] != "_":
                j+=1 
            
            count = int(s[i:j])
            i = j + 1
            j = i + count
            res.append(s[i:j])
            i = j
        return res
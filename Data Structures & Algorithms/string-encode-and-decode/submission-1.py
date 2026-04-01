class Solution:
    #4_neet4_code4_love3_you
    #012345678
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "_" + s
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 

            while s[j] != "_":
                j += 1
            count = int(s[i:j])
            i = j + 1
            j = i + count
            res.append(s[i:j])
            i = j 
        return res
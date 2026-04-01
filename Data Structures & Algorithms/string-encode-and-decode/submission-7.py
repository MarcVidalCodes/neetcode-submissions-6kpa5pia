class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs: 
            encoded += str(len(s)) + '_' + s
        return encoded
        # 4_leet4_code

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[i] != '_':
                i += 1
            
            count = int(s[j:i])
            i += 1
            j = i + count
            res.append(s[i:j])
            i = j
        return res


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 0: 
            return []

        anagrams = {} 

        for s in strs: 
            string = ''.join(sorted(s))

            if not string in anagrams: 
                anagrams[string] = [] 

            anagrams[string].append(s)
        res = [value for value in anagrams.values()]
        return res
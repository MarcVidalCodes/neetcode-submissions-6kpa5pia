class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} 
        #key, value
        #sorted string, array of string

        for string in strs:
            sortedString = ''.join(sorted(string))
            groups.setdefault(sortedString, []).append(string)
        
        return list(groups.values())
            

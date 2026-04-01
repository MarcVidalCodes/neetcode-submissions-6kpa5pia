class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string = defaultdict(list)

        #sortedString, string 
        for s in strs: 
            sortedString = ''.join(sorted(s))
            string[sortedString].append(s)
        
        return list(string.values())
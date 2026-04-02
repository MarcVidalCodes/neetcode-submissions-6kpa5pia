class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set() 
        longest_substring = 0
        l = 0 

        for r in range(len(s)): 
            while s[r] in substring: 
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
        return longest_substring
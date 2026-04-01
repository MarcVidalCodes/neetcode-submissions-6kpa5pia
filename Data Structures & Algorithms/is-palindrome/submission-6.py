class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for i in range(len(s)):
            if(s[i].isalnum()):
                string += s[i].lower()
    
        ptr1 = 0 
        ptr2 = len(string) - 1

        while ptr1 <= ptr2: 
            if string[ptr1] == string[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else: 
                return False
        return True
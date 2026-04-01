class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower() 

        front = 0
        back = len(string) - 1

        while front < back:
            if not string[front].isalnum():
                front += 1
                continue
            
            if not string[back].isalnum():
                back -= 1
                continue

            if string[front] != string[back]:
                return False

            front += 1
            back -= 1
        return True
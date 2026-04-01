class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length()-1; 

        while(l < r){
            while(l<r && !isAlNum(s.charAt(l))){
                l++;
            }

            while(r>l && !isAlNum(s.charAt(r))){
                r--;
            }

            if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false; 
            }
            r--;
            l++; 
        }
        return true; 
    }

    public boolean isAlNum(char c){
        return(c>='0' && c<='9' || c>='a' && c<='z' ||c>='A' && c<= 'Z');
    }
}

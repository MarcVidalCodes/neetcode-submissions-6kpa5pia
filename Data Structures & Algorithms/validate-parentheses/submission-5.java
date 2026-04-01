class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>(); 
        char[] string = s.toCharArray(); 

        for(int i=0; i<string.length; i++){
            char ch = string[i];
            if(ch == '{' || ch =='(' || ch=='['){
                stack.push(ch);
            }else{ 
            if(stack.size() == 0) return false; 
            char top = stack.peek(); 
            if(((ch == ')' && top == '(')||(ch == '}' && top == '{')||(ch == ']' && top == '['))){
                stack.pop(); 
            }else{
                return false; 
            }
            }
        }
        return stack.isEmpty(); 
    }
}

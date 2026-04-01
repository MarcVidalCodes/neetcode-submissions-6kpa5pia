class Solution {
    public boolean isAnagram(String s, String t) {
        Hashtable<Character, Integer> hs = new Hashtable<>();
        Hashtable<Character, Integer> ht = new Hashtable<>();

        for(int i =0; i<s.length(); i++){
            if(s.length() != t.length()){
                return false; 
            }

            hs.put(s.charAt(i), hs.getOrDefault(s.charAt(i),0)+1);
            ht.put(t.charAt(i), ht.getOrDefault(t.charAt(i),0)+1);
        }
        return hs.equals(ht);
    }
}

class Solution {
    public String longestPalindrome(String s) {
        if(s.length() == 1){
            return s;
        }
        int max = 0;
        String maxStr = "";
        for(int i = 0; i <= s.length(); i ++){
            for(int j = 0; j < i; j ++){
                String sub = s.substring(j, i);
                if( ifPali(sub)){
                    if (sub.length() >= max){
                        max = sub.length();
                        maxStr = sub;
                    }
                }
            }
        }
        return maxStr;
    }


    public boolean ifPali(String s){

        int l = s.length();
        for (int i = 0; i < l/2; i++)
            if(s.charAt(l - i - 1)  != s.charAt(i)){
                return false;
            }

        return true;

    }
}
class Solution {
    fun isPalindrome(x: Int): Boolean {
        if(x < 0){
            return false
        }else{
            var s: String = x.toString()

            for(i in 0 .. s.length / 2){
                if(s[i] != s[s.length - i - 1]){
                    return false
                }
            }
            return true

        }
    }
}
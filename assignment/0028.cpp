class Solution {
public:
    int strStr(string haystack, string needle) {

        if(needle.size() == 0){
            return 0;
        }
        for (int i = 0; i < haystack.size(); i++){
            for(int j = 0; j < needle.size(); j++){
                if(haystack[i + j] == needle[j]){
                    if(j == needle.size() - 1){
                        return i;
                    }else{
                        continue;
                    }
                }else{
                    break;
                }

            }
        }
        return -1;
    }
};
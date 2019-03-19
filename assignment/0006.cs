public class Solution {
    public string Convert(string s, int numRows) {
        if( numRows == 1){
            return s;
        }
        List<List<char>> zigzag = new List<List<char>>();
        for(int i = 0; i < numRows; i++){
           zigzag.Add( new List<char>());
        }
        int index = 0;
        int m = numRows * 2 - 2;

        foreach (char c in s){
            int md = index % m;
            if (md < numRows){
                zigzag[md].Add(c);
            }else{
                zigzag[m - md ].Add(c);
            }
            index ++;
        }
        string ret = "";
        foreach (List<char> l in zigzag){
            foreach(char c in l){
                ret += c;
            }

        }
        return ret;
        // zigzag[0].Add("2");
        // return "";
    }
}
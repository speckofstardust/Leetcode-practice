import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] _s=s.toCharArray();
        char[] _t=t.toCharArray();
        Arrays.sort(_s);
        Arrays.sort(_t);
        s=Arrays.toString(_s);
        t=Arrays.toString(_t);
        if(s.equals(t))
            return true;
        else
            return false;
    }
}

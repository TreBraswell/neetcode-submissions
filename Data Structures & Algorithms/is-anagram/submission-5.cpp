#include <unordered_set>
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> s_set;
        std::unordered_map<char,int> t_set;
        if(s.size() != t.size())
        {
            return false;
        }
        for(int i = 0; i <s.size(); i++)
        {
            s_set[s[i]]++;
            t_set[t[i]]++;
        }
        if(s_set==t_set){
            return true;
        }
        return false;
    }
};

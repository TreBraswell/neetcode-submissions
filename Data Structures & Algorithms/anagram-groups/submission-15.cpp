class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<string,vector<string>> res;
        for(string s : strs){
            string sorted = [](string& input) -> string{
                string sorted = input;
                sort(sorted.begin(),sorted.end());
                return sorted;
            }(s);
            res[sorted].push_back(s);
        }
        vector<vector<string>> res_complete;
        for (auto n : res)
        {
            res_complete.push_back(n.second);
        }
        return res_complete;

    }
};

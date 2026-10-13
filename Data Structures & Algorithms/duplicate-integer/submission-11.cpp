class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> h;
        for(int i : nums)
        {
            if(h.contains(i)){
                return true; 
            }
            h.insert(i);
        }
        return false;
    }
};
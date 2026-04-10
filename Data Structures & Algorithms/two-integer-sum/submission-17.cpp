class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> h_map;
        for(int i = 0; i <nums.size(); i++)
        {
            auto val = target - nums[i];
            if (h_map.find(val) != h_map.end()){
                return {h_map[val],i};
            }

            h_map[nums[i]] = i;

        }
        return {};
    }
};

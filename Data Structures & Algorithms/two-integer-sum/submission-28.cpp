class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int,int> res;

        for(int i = 0; i <nums.size();i++ )
        {
            
            if(res.contains(target- nums[i])){

                return {res[target- nums[i]], i};
            }
            res[nums[i]]=i;

        }
    }
};

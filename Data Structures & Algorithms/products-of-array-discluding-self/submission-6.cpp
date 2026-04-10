class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(),1);
        int s = 1;
        for(int i = 0; i < nums.size()-1; i ++)
        {
            s = s * nums[i];
            res[i+1] = s;
        }
        s = 1;
        for(int i = nums.size()-1; i > 0; i --)
        {
            s = s * nums[i];
            res[i-1] = s * res[i-1];
        }
        return res;
    }
};

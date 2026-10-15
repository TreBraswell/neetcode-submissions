class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() -1;
        int res = 0;
        while (l<r)
        {
            auto mn = min(heights[l],heights[r]);
            auto temp = mn * (r-l);
            res = max(res,temp);
            if (heights[r]> heights[l])
            {
                l++;
            }
            else
            {
                r--;
            }

        }
        return res;
    }
};

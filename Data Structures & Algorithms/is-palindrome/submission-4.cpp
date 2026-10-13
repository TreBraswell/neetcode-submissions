class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size()-1;
        while (l<r)
        {
            if(!std::isalnum(static_cast<unsigned char>(s[l])))
            {
                l++;
                continue;

            }
            if(!std::isalnum(static_cast<unsigned char>(s[r])))
            {
                r--;
                continue;
                
            }
            if (std::tolower(static_cast<unsigned char>(s[l])) != std::tolower(static_cast<unsigned char>(s[r])))
            {
                return false;
            }
            l++;
            r--;
        }
        return true;

    }
};

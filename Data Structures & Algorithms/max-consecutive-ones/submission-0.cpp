class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int cur = 0;
        for(const int n : nums) {
            if (n == 1) {
                cur++;
                ans = max(ans, cur);
            } else {
                cur = 0;
            }
        }
        return ans;
    }
};
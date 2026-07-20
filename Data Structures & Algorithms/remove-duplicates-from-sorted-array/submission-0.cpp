class Solution {
   public:
    int removeDuplicates(vector<int>& nums) {
        int w{1};
        for (int r{1}; r < nums.size(); ++r) {
            if (nums[r] != nums[r - 1]) {
                nums[w++] = nums[r];
            }
        }

        return w;
    }
};
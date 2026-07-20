/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
   public:
    bool isBalanced(TreeNode* root) {
        auto dfs = [&](this auto self, TreeNode* root) -> tuple<bool, int> {
            if (!root) {
                return {true, 0};
            }

            tuple<bool, int> left = self(root->left);
            tuple<bool, int> right = self(root->right);

            bool balanced = (std::get<bool>(left) and std::get<bool>(right)) and
                            (abs(std::get<int>(left) - std::get<int>(right)) <= 1);

            int height = 1 + max(std::get<int>(left), std::get<int>(right));

            return {balanced, height};
        };

        return std::get<bool>(dfs(root));
    }
};

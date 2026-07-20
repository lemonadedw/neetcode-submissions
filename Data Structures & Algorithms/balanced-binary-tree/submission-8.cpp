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
        auto dfs = [&](this auto self, TreeNode* root) -> pair<bool, int> {
            if (!root) {
                return {true, 0};
            }

            auto [left_balanced, left_height] = self(root->left);
            auto [right_balanced, right_height] = self(root->right);

            bool balanced =
                left_balanced && right_balanced && (std::abs(left_height - right_height) <= 1);

            int height = 1 + std::max(left_height, right_height);

            return {balanced, height};
        };

        return dfs(root).first;
    }
};

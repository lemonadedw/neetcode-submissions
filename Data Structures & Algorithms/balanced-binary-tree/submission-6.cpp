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
        if (!root){
            return true;
        }

        auto height = [&](this auto self, TreeNode* root) -> int {
            if (!root) {
                return 0;
            }

            return 1 + max(self(root->left), self(root->right));
        };

        if (abs(height(root->left) - height(root->right)) > 1){
            return false;
        }

        return (isBalanced(root->left) && isBalanced(root->right));
    }
};

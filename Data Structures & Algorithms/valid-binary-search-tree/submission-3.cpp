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
    bool isValidBST(TreeNode* root) {
        auto valid = [&](this auto self, TreeNode* node, int l, int h) -> bool {
            if (!node) return true;
            if (node->val <= l or node->val >= h) return false;

            return self(node->left, l, node->val) and self(node->right, node->val, h);
        };

        return valid(root, -1001, 1001);
    }
};

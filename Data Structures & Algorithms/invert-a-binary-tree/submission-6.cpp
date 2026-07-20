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

#include <utility>

class Solution {
   public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) {
            return nullptr;
        }

        std::vector<TreeNode*> s{};
        s.push_back(root);

        while (s.size()) {
            TreeNode* node = s.back();
            s.pop_back();

            std::swap(node->left, node->right);
            if (node->left) {
                s.push_back(node->left);
            }
            if (node->right) {
                s.push_back(node->right);
            }
        }

        return root;
    }
};

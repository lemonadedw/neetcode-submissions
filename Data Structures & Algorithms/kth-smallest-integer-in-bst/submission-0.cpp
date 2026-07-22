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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> l{};
        
        auto dfs = [&](this auto self, TreeNode* node) -> void{
            if (!node) return;

            self(node->left);
            l.push_back(node->val);
            self(node->right);
        };

        dfs(root);

        return l[k - 1];
    }
};

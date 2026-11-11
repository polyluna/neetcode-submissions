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
        int min = -1200;
        int max = 1200;
        return validate(root, min, max);

    }
    bool validate(TreeNode* node, int min, int max) {
        if (node == nullptr) return true;
        return (min < node->val && node->val < max 
        && validate(node->left,min,node->val) && 
        validate(node->right,node->val,max));
    } 
};

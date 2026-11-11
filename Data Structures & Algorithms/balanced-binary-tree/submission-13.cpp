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
        return height(root) != -1;
        
    }
    int height(TreeNode* node) {
        if (node == nullptr) return 0;

        int hL = height(node->left);
        int hR = height(node->right);

        if (abs(hL - hR) >= 2) {
            return -1;
        }

        if (hL == -1 || hR == -1) {
            return -1;
        }

        

        return max(hL,hR) + 1;
    }
};

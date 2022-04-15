'''
669. Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

https://leetcode.com/problems/trim-a-binary-search-tree/
'''
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    
        def prune(node):
            if not node:
                return None
            
            if node.val > high:
                return prune(node.left)
            
            if node.val < low:
                return prune(node.right)
            
            node.left = prune(node.left)
            node.right = prune(node.right)
             
            return node
        
        return prune(root)
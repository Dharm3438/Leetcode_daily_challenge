# 897. Increasing Order Search Tree

# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node 
# in the tree is now the root of the tree, and every node has no left child and only one right child.

# https://leetcode.com/problems/increasing-order-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root, tail = None):
        if not root:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
        
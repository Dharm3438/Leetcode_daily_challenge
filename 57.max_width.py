'''
662. Maximum Width of Binary Tree

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

https://leetcode.com/problems/maximum-width-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        if not root: return []
        width, level = 0, [(root, 1)]
        # Keep going untill current level has some nodes.
        while len(level):
            # Put all children of current level in next_level.
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:   # Make sure to not put the Null nodes
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2+1))
            level = next_level
        return width
        
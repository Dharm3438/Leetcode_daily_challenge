'''
1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        values = []
        def collect(root):
            if root:
                collect(root.left)
                values.append(root.val)
                collect(root.right)
        collect(root1)
        collect(root2)
        return sorted(values)
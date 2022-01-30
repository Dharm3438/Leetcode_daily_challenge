'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

https://leetcode.com/problems/rotate-array/
'''
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
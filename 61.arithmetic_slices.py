'''
413. Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

https://leetcode.com/problems/arithmetic-slices/
'''

class Solution:
    def numberOfArithmeticSlices(self, A):
        le=len(A)
        l=[0]*(le)
        for i in range(2,le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                l[i]=1+l[i-1]
        return sum(l)
        
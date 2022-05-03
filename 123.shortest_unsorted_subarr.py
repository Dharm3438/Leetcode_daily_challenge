# 581. Shortest Unsorted Continuous Subarray

# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray 
# in ascending order, then the whole array will be sorted in ascending order.

# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
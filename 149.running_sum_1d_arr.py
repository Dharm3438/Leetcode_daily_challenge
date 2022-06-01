# 1480. Running Sum of 1d Array

# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums):
        i = 1
        while i<len(nums):
            nums[i]+=nums[i-1]
            i+=1
        return nums
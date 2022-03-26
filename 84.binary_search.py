'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/binary-search/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end=len(nums)-1
        mid = (start+end)//2
        
        while(start<=end):
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                start = mid+1
            else:
                end=mid-1
            mid = (start+end)//2
    
        return -1
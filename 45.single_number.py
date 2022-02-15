'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

https://leetcode.com/problems/single-number/'

we use bitwise XOR to solve this problem :

first , we have to know the bitwise XOR in java

0 ^ N = N
N ^ N = 0
So..... if N is the single number

N1 ^ N1 ^ N2 ^ N2 ^..............^ Nx ^ Nx ^ N

= (N1^N1) ^ (N2^N2) ^..............^ (Nx^Nx) ^ N

= 0 ^ 0 ^ ..........^ 0 ^ N

= N

The key t this problem is every elements occurs twice so n^n will give 0 
and at last we remain with one n^0=n
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            ans=ans^nums[i]
            
        return ans
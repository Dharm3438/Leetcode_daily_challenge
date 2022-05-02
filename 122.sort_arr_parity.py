# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start=0
        end=len(A)-1
        while start < end:
            if A[start] % 2 == 0:
                start += 1
            elif A[end] % 2 != 0:
                end -= 1
            else:
                A[start], A[end] = A[end], A[start]
        return A
        
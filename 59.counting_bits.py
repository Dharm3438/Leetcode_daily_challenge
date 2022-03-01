'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

https://leetcode.com/problems/counting-bits/
'''

'''
Analysis
To understand the solution, we remember the following two points from math:

All whole numbers can be represented by 2N (even) and 2N+1 (odd).
For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when multiplying by ten in base 10).
Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. Likewise, doubling a number and adding one will increase the count by exactly 1. Or:

countBits(N) = countBits(2N)
countBits(N)+1 = countBits(2N+1)
Thus we can see that any number will have the same bit count as half that number, with an extra one if it's an odd number. We iterate through the range of numbers and calculate each bit count successively in this manner:
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[0]*(n+1)
        for i in range(n+1):
            arr[i] = arr[i >> 1] + i % 2
        return arr
        
'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

https://leetcode.com/problems/add-binary/
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result = str(carry %2) + result
            carry //= 2

        return result
        
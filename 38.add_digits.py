'''
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

https://leetcode.com/problems/add-digits/
'''
class Solution:
    def addDigits(self, num: int) -> int:
        val = str(num)
        while(len(val)>1):
            sumi=0
            for i in val:
                sumi+=int(i)
            val=str(sumi)
        return val
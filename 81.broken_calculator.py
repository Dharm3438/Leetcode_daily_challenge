'''
991. Broken Calculator

There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

https://leetcode.com/problems/broken-calculator/submissions/
'''

class Solution:
    def helper(self, start,target):
        if(start>=target):
            return start-target
        
        if(target%2==0):
            return 1+self.helper(start,target//2)
        else:
            return 1+self.helper(start,target+1)
        
    def brokenCalc(self, startValue: int, target: int) -> int:
        if(startValue>=target):
            return startValue-target
        
        return self.helper(startValue,target)
        
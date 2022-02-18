'''
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

https://leetcode.com/problems/remove-k-digits/
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while( stack and int(stack[-1]) > int(n) and k):
                stack.pop()
                k -= 1
            stack.append(str(n))
        
        while(k):
            stack.pop()
            k -= 1
            
        i = 0
        while( i <len(stack) and stack[i] == "0" ):
            i += 1
            
        return ''.join(stack[i:]) if (len(stack[i:]) > 0) else "0" 
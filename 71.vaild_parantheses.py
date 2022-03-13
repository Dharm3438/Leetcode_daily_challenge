'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if(i=='(' or i=='[' or i=='{'):
                stk.append(i)
            else:
                if(len(stk)>=1):
                    if(stk[-1]=='(' and i==')'):
                        stk.pop()
                    elif(stk[-1]=='[' and i==']'):
                        stk.pop()
                    elif(stk[-1]=='{' and i=='}'):
                        stk.pop()
                    else:
                        return False
                else:
                    return False
        if(len(stk)==0):
            return True
        else:
            return False
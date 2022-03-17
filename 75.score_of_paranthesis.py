'''
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

https://leetcode.com/problems/score-of-parentheses/
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        stack.append(0)
        for i in s:
            if i =='(':
                stack.append(0)
            else:
                tmp=stack.pop()
                val=0
                if(tmp>0):
                    val=tmp*2
                else:
                    val=1
                stack[-1] +=val
                
        return stack[-1]
                
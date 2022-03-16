'''
946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

https://leetcode.com/problems/validate-stack-sequences/

Basic simulation of stack

Loop through the pushed array,
    1) Keep pushing pushed elements into stack if the top element on the stack is different from the current one of popped;
    2) Keep poping out of the top element from stack if it is same as the current one of popped;
    3) Check if the stack is empty after loop.
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        idx = 0
        stack = []
        
        for p in pushed:
            stack.append(p)
            while stack and stack[-1]==popped[idx]:
                stack.pop()
                idx+=1

        return not stack
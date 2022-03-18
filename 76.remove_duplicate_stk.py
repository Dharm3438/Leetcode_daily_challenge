'''
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

https://leetcode.com/problems/remove-duplicate-letters/
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occ = {}
        stack = []
        
        for i in range(len(s)):
            last_occ[s[i]] = i
    
        for i in range(len(s)):
        
            if s[i] not in stack:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    stack.pop()
    
                stack.append(s[i])
                
        return ''.join(stack)
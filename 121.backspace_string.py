# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])
        
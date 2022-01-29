'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[-1]
        ans=0
        n=len(heights)
        for i in range(n):
            while(heights[i]<heights[stack[-1]]):
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                ans=max(ans,h*w)
            stack.append(i)
        heights.pop()
        return ans            
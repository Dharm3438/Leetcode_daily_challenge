'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(len(matrix)==0):
            return False
        
        n = len(matrix)
        m=len(matrix[0])
        
        low = 0
        high = (n*m)-1
        
        while(low<=high):
            mid = low+(high-low)//2
            
            if(matrix[mid//m][mid%m] == target):
                return True
            elif(matrix[mid//m][mid%m]<target):
                low = mid+1
            else:
                high=mid-1
            
            
        return False
            
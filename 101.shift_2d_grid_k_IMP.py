'''
1260. Shift 2D Grid

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

https://leetcode.com/problems/shift-2d-grid/
'''

'''
Solution Approach 
/* multiplying total number of columns into current row number (n*i) plus current column ( n*i + j ) gives us the current index number of element in a 1D array, adding k will increase the index number in 1D array (n*i + j + k) */

/* Now convert it into the 2D array index by finding the updated row and column for the element, dividing by total column numbers should provide us the current row, taking modulo by m to make sure the result exists between 0 to m-1 */

/* Finding the current column number is easy, taking modulo will provide us the updated column number between 0 to n-1 */

'''

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        #modifying k according to single array index
        k = k%(m*n)
        
        ans = [[-1 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                ind = (i*n + j+k) 
                
                x = ind//n%m
                
                y = ind%n
                
                ans[x][y]=grid[i][j]
                
        return ans
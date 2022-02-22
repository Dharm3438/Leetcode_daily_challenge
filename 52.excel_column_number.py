'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

https://leetcode.com/problems/excel-sheet-column-number/
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans


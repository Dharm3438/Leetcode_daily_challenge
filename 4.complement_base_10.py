'''
1009. Complement of Base 10 Integer

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

https://leetcode.com/problems/complement-of-base-10-integer/
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        val = bin(n).replace("0b","")
        res=''
        for i in val:
            if(i=='1'):
                res+='0'
            else:
                res+='1'
        #print(val,type(val))
        #print(res)
        
        return int(res,2)

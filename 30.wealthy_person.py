'''
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

https://leetcode.com/problems/richest-customer-wealth/
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=-999999999
        for i in accounts:
            tmp=sum(i)
            ans=max(ans,tmp)
        
        return ans
        

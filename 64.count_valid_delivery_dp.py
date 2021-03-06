'''
1359. Count All Valid Pickup and Delivery Options

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
'''

class Solution:
    def countOrders(self, n):
        res, mod = 1, 10**9 + 7
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) // 2 % mod
        return res
        
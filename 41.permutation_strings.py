'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

https://leetcode.com/problems/permutation-in-string/
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False
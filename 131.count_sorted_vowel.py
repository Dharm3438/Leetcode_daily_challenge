# 1641. Count Sorted Vowel Strings

# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24;
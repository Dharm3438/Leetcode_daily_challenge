'''
520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

https://leetcode.com/problems/detect-capital/
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ct=0
        for i in word:
            if i.isupper():
                ct+=1
        if ct==1 and word[0].isupper():
            return True 
        elif ct==0:
            return True 
        elif ct==len(word):
            return True 
        else:
            return False
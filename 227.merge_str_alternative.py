class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        for i in range(min(len(word1),len(word2))):
            res+=word1[i]+word2[i]
        
        if(i+1<len(word1)):
            res+=word1[i+1:]
        elif(i+1<len(word2)):
            res+=word2[i+1:]
        return res

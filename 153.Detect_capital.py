class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ct = 0
        for i in word:
            if i.isupper():
                ct+=1
        
        if(ct==len(word) or ct==0):
            return True
        else:
            if(ct==1 and word[0].isupper()):
                return True
            return False

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        #Count the no of zeros and store in ans
        ct = 0
        for i in s:
            if i=='0':
                ct+=1
        
        #For every zeros decrease the count and increase for ones
        ans = ct
        for i in s:
            if i=='0':
                ct-=1
                ans = min(ans,ct)
            else:
                ct+=1
        
        return ans

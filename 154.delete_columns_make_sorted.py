class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n = len(strs)
        m = len(strs[0])
        ct = 0

        for j in range(m):
            for i in range(1,n):
                if(strs[i-1][j]>strs[i][j]):
                    ct+=1
                    break

        return ct      

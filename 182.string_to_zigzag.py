class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if(numRows==1):
            return s

        mat = [[-1 for i in range(len(s))] for j in range(numRows)]
        # print(mat)

        i = 0
        row = 0
        col = 0
        while(i<len(s)):
            while(row<numRows and i<len(s)):
                mat[row][col] = s[i]
                i+=1
                row+=1
            
            row = numRows-2
            col+=1

            while(row>0 and i<len(s)):
                mat[row][col] = s[i]
                i+=1
                row-=1
                col+=1


        ans = ''
        for i in range(numRows):
            for j in range(len(s)):
                if(mat[i][j]!=-1):
                    ans+=mat[i][j]

        # for val in mat:
        #     print(val)
            
        return ans

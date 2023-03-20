class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        ans = 0
        size = len(flowerbed)
        while(i<size):
            if(flowerbed[i]==1):
                i+=2
            else:
                if(i<size-1 and flowerbed[i+1]!=1):
                    flowerbed[i] = 1
                    ans+=1
                    i+=2
                else:
                    i+=1
                
        if(flowerbed[size-1]==0 and flowerbed[size-2]==0):
            ans+=1
        
        if(ans>=n):
            return True
        
        return False

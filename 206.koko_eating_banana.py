class Solution:
    
    def possible(self,piles,h,mid):
        ct = 0
        for i in piles:
            ct+=math.ceil(i/mid)
        
        if(ct<=h):
            return True
        return False
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        
        while(start<=end):
            mid = start+(end-start)//2
            if(self.possible(piles,h,mid)):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        
        return ans

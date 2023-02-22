class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def ispossible(weights,days,mid):
            sumi = 0
            ct=1
            for i in range(len(weights)):
                if(sumi+weights[i]<=mid):
                    sumi+=weights[i]
                else:
                    
                    sumi = weights[i]
                    if(sumi>mid):
                        return False
                    ct+=1
            
            if(ct<=days):
                return True
            else:
                return False
        
        # weights.sort()
        start = weights[0]
        end = sum(weights)
        ans = -1
        while(start<=end):
            mid = start+(end-start)//2
            if(ispossible(weights,days,mid)):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans

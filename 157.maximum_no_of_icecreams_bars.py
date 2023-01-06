class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ct = 0

        for val in costs:
            if(val<=coins):
                coins-=val
                ct+=1
            else:
                break

        return ct
        

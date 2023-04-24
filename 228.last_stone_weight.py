import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for val in stones:
            heapq.heappush(heap,-1*val)
        
        while(len(heap)>=2):
            first_max = heapq.heappop(heap)
            second_max = heapq.heappop(heap)
            new_stone = (-1*first_max)-(-1*second_max)
            if(new_stone==0):
                pass
            else:
                heapq.heappush(heap,-1*new_stone)
        
        if(len(heap)==0):
            return 0
        
        return heap[0]*-1

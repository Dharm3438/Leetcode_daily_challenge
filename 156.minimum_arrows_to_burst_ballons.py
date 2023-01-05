class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        cur = points[0][1]
        ct = 1
        for i in range(1,len(points)):
            if(cur>=points[i][0]):
                continue
            ct+=1
            cur = points[i][1]
        
        return ct

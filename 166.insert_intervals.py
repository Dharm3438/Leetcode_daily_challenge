class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()

        print(intervals)
        stk=[]
        for interval in intervals:
            if((len(stk)==0) or (len(stk) and stk[-1][1]<interval[0])):
                stk.append(interval)
            else:
                if(len(stk)):
                    tmp = stk.pop()
                    tmp[0] = min(tmp[0],interval[0])
                    tmp[1] = max(tmp[1],interval[1])
                    stk.append(tmp)
        return stk

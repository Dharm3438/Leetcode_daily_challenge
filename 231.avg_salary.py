import math
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        maxi = -1E9
        mini = 1E9
        
        sumi = 0.0
        for i in salary:
            sumi+=i
            maxi = max(maxi,i)
            mini = min(mini,i)
    
        return (sumi-maxi-mini)/(len(salary)-2)

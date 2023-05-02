class Solution(object):
    def signFunc(self,num):
        if(num==0):
            return 0
        elif(num>0):
            return 1
        elif(num<0):
            return -1
        
    
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = 1
        for val in nums:
            prod *= val
        
        print(prod)
        
        return self.signFunc(prod)

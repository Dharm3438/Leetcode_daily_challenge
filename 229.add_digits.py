class Solution:
    def addDigits(self, num: int) -> int:
        val = str(num)
        while(len(val)>1):
            sumi=0
            for i in val:
                sumi+=int(i)
            val=str(sumi)
        return val

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        nums.append('#')
        ct = 1
        ans = []
        
        for i in range(len(nums)-1):
            if(nums[i]==0 and nums[i+1]==0):
                ct+=1
            else:
                if(ct!=1):
                    ans.append(ct)
                ct = 1
        print(ans)

        res=0
        for val in ans:
            res+=(val*(val+1))//2

        sumi = sum(ans)
        count = nums.count(0)
        if(sumi!=count):
            tmp = count-sumi
            res+=tmp

        return res

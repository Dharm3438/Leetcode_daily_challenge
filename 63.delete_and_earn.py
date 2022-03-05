'''
740. Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

https://leetcode.com/problems/delete-and-earn/

https://leetcode.com/problems/delete-and-earn/discuss/777526/Java-Recursive-greater-Memoization-greater-Bottom-Up

- For each of the numbers 'x', we have a choice of picking the number and skipping the next number 'x + 1' OR
	  skip the number 'x'
	- The total number of points we can get for picking 'x' is equal to 'x * frequency(x)'
	- Since, we want to earn the most points
		- We will want to pick the choice that will give us a higher number of points
- We will need to create an array 'count' to store the frequency of each number
'''
#MEMOIZED SOLUTION NEED TO WORK ON TABULATION

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0]*10001
        dp = [-1]*10001
        maxNum = 0
        
        for num in nums:
            count[num]+=1
            maxNum = max(maxNum,num)
            
        def helper(num,count,dp):
            if(num<=0):
                return 0
            
            if(dp[num]!=-1):
                return dp[num]
            
            pick = helper(num-2,count,dp) + (num*count[num])
            nonpick = helper(num-1,count,dp)
            
            dp[num] = max(pick,nonpick)
            
            return dp[num]
        
        return helper(maxNum, count, dp)
        
        

        
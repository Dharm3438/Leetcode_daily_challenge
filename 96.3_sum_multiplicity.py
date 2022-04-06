'''
923. 3Sum With Multiplicity

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

https://leetcode.com/problems/3sum-with-multiplicity/
'''

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ct = 0
        for k in range(0,len(arr)-2):
            i=k+1
            j=len(arr)-1
            while(i<j):
                if(arr[i]+arr[j]+arr[k]==target):
                    print(arr[k],arr[i],arr[j])
                    ct+=1
                    i+=1
                elif(arr[i]+arr[j]<target):
                    i+=1
                else:
                    j-=1
        return ct
'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

https://leetcode.com/problems/top-k-frequent-elements/
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = dict()
        for i in nums:
            if i in store:
                store[i]+=1
            else:
                store[i]=1
        
        store = sorted(store.items(), key=lambda x:x[1], reverse=True)
        
        ans=[]
        for i in range(k):
            ans.append(store[i][0])
    
        return ans
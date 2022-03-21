# 763. Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# https://leetcode.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store=dict()
        
        for i in range(len(s)):
            store[s[i]] = i
        
        ans=[]
        prev=-1
        maxi=0
        
        for i in range(len(s)):
            maxi = max(maxi,store[s[i]])
            if(maxi==i):
                ans.append(maxi-prev)
                prev=maxi

        return ans
                
        
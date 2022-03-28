'''
81. Search in Rotated Sorted Array II

Same as searching in rotated sorted array but the elements are not distinct
eg- [2,5,6,0,0,1,2]     [4,5,6,6,7,0,1,2,4,4]
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high = len(nums)-1
        while(low<=high):
            mid = low+(high-low)//2
            if(target==nums[mid]):
                return True
            ##This if is necessary because elements are not distinct
            if(nums[low]==nums[mid] and nums[mid]==nums[high]):
                low+=1
                high-=1
            elif(nums[low]<=nums[mid]):
                if(target>=nums[low] and target<=nums[mid]):
                    high=mid-1
                else:
                    low=mid+1
            else:
                if(target>=nums[mid] and target<=nums[high]):
                    low=mid+1
                else:
                    high=mid-1
            
        return False
                
                
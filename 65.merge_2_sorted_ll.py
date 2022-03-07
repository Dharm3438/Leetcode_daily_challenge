'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

https://leetcode.com/problems/merge-two-sorted-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1==None):
            return list2
        if(list2==None):
            return list1
        
        if(list1.val<=list2.val):
            fh=list1
            ft=list1
            list1=list1.next
        else:
            fh=list2
            ft=list2
            list2=list2.next
        
        while(list1!=None and list2!=None):
            if(list1.val<=list2.val):
                ft.next=list1
                ft=list1
                list1=list1.next
            else:
                ft.next=list2
                ft=list2
                list2=list2.next
                
        if(list1==None):
            ft.next = list2
        if(list2==None):
            ft.next = list1

        return fh
            
            
        
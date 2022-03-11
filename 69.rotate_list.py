'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

https://leetcode.com/problems/rotate-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        if(k<=0):
            return head
        ct=0
        itr=head
        while(itr!=None):
            ct+=1
            prev=itr
            itr=itr.next
        #print(ct)
        
        k=k%ct
        if(k<=0):
            return head
        val=ct-k
        #print(val)
        ct2=0
        itr=head
        while(itr!=None):
            if(ct2==val-1):
                head2=itr.next
                itr.next=None
                break
            ct2+=1
            itr=itr.next
            
        prev.next=head
        
        return head2
            
        
        
            
        
// 148. Sort List

// Given the head of a linked list, return the list after sorting it in ascending order.

// https://leetcode.com/problems/sort-list/

// https://leetcode.com/problems/sort-list/discuss/46714/Java-merge-sort-solution

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        
        ListNode prev=null,slow,fast;
        slow=head;
        fast=head;
        
        while(fast!=null || fast.next!=null){
            prev=slow;
            slow=slow.next;
            fast=fast.next.next;
        }
        
        prev.next=null;
        
        ListNode l1 = sortedList(head);
        ListNode l2 = sortedList(slow);
        
        return merge(l1,l2);
        
    }
    public ListNode merge(ListNode l1, ListNode l2){
        
        ListNode l = new ListNode(0), p = l;
        
        while(l1!=null and l2!=null){
            if(l1.val>l2.val){
                p.next = l2;
                l2=l2.next;
            }
            else{
                p.next = l1;
                l1=l1.next;
            }
            p=p.next;
        }
        
        if (l1 != null)
            p.next = l1;
    
        if (l2 != null)
            p.next = l2;
    
        return l.next;
    }
}
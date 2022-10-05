# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        
        list_len, last = self.get_len_last(head)
        k = k % list_len
        
        if k == 0:
            return head
        
        new_last = head
        for i in range(list_len - k - 1):
            new_last = new_last.next
            
        last.next = head
        new_first = new_last.next
        new_last.next = None
        
        return new_first
        
    def get_len_last(self, head):
        count = 1
        n = head
        while n.next is not None:
            n = n.next
            count += 1
        return count, n
        
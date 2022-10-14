# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """       
        n = self.get_len(head)
        if n <= 1:
            return None
        
        s = self.get_mid(head, n)
        m = s.next
        e = m.next
        m.next = None
        s.next = e
        return head
        
        
    def get_mid(self, head, n):
        for i in range(1, n/2):
            print head.val
            head = head.next
        return head
        
    def get_len(self, head):
        n = 0
        while head is not None:
            head = head.next
            n += 1
        return n
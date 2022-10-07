# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = 0
        res = None
        
        head1 = l1
        head2 = l2
        while head1 is not None and head2 is not None:
            if res is None:
                res = index = ListNode()
            else:
                index.next = ListNode()
                index = index.next
            v = head2.val + head1.val + r
            index.val = v % 10
            r = v / 10
            
            head1 = head1.next
            head2 = head2.next
            
        
        head = head1 if head1 is not None else head2
        if head is not None:
            while head is not None:
                index.next = ListNode()
                index = index.next
                v = head.val + r
                index.val = v % 10
                r = v / 10
                head = head.next
                
        if r != 0:
                index.next = ListNode()
                index = index.next
                index.val = r
                
        return res
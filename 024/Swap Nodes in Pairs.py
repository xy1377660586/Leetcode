# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        while head and head.next:
            temp=head.next.next
            cur.next=head.next
            cur.next.next=head
            head.next=temp
            cur=head
            head=temp
        return dummy.next

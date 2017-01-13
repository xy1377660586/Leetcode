# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
   def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newlist=[]
        p=head
        while p:
            newlist.insert(0, p.val)
            p=p.next
        p=head
        for i in newlist:
            p.val=i			
            p=p.next
			
        return head		

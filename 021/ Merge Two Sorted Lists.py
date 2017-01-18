# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if l1==None:
			return l2
		if l2==None:
			return l1
		if l1==None and l2==None:
			return None
		dump=ListNode(0)
		temp=dump
		while l1 and l2:
			if l1.val<=l2.val:
				temp.next=l1
				l1=l1.next
				temp=temp.next
			else:
				temp.next=l2
				l2=l2.next
				temp=temp.next

		if l2==None:
			temp.next=l1
		else:
			temp.next=l2
		return dump.next



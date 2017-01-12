# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		while headA:
				headA=headA.next
				headB=headB.next
		for i in range(3):
			headB=headB.next#为什么会有这种奇葩的报错！！！！
###################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		if headA==None or headB==None:
			return None

		listA=[]
		listB=[]
		
		while 1:
			if headA==None:
				break;
			listA.append(headA.val)
			headA=headA.next

		while 1:
			if headB==None:
				break;
			listB.append(headB.val)
			headB=headB.next


		if listA[-1]!=listB[-1]:
			return None;

		if len(listA)<len(listB):
			diff=len(listB)-len(listA)
			
			for i in range(diff):
				headB=headB.next	
			while headA:
				headA=headA.next
				headB=headB.next
				if headA.val==headB.val:
					return headA.val
				else:
					return None;


	

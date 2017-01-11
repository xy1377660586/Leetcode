\后来找到了复杂度O(n)的方法，使用两个指针slow,fast。两个指针都从表头开始走，slow每次走一
步，fast每次走两步，如果fast遇到null，则说明没有环，返回false；如果slow==fast，说明有环，并且此时
fast超了slow一圈，返回true
为什么有环的情况下二者一定会相遇呢？因为fast先进入环，在slow进入之后，如果把slow看作在前
面，fast在后面每次循环都向slow靠近1，所以一定会相遇，而不会出现fast直接跳过slow的情况

快慢指针

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def hasCycle(self, head):
		
		if head==None or head.next==None:
			return False
			
		q,s=head,head
		while q and q.next: # 注意这个条件，如果只是用while q.next 是不可以的
		#这是英文这两指针， P 和s 中的p 是每次走两步的，所以的话，q！=None和q.next！=None必须同时满足
			q=q.next.next
			
			s=s.next

			if q==s:
				return True
		return False

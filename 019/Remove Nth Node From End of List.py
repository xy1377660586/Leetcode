# Definition for singly-linked list.
# class ListNode(object): 这个函数是干嘛的啊？？初始化linked list？
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)  
        dummy.next = head #为什么dummy.next 是头指针？
        p, q = dummy, dummy  
          
        # first 'q' go n step  
        for i in range(n):  
            q = q.next  
  
        # q & p  
        while q.next:  
            p = p.next  
            q = q.next  
  
        rec = p.next  
        p.next = rec.next#有什么用啊？  
        del rec  
        return dummy.next 

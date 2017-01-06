    class Solution:  
        # @return a ListNode  
        def removeNthFromEnd(self, head, n):  
            dummy = ListNode(0)  
            dummy.next = head  
            p, q = dummy, dummy  
              
            # first 'q' go n step  
            for i in range(n):  
                q = q.next  
      
            # q & p  
            while q.next:  
                p = p.next  
                q = q.next  
      
            rec = p.next  
            p.next = rec.next  
            del rec  
            return dummy.next  

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        delflag = 1
        flag = 1
        p = head
        while(p != None and p.next != None):
            if p.val != p.next.val:
                flag = 1
                p = p.next
            elif flag < delflag:
                flag += 1;
                p = p.next
            else:
                p.next = p.next.next
        return head

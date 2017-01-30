class Solution(object):
    def merge(self, A, m, B, n): 
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        x=A[0:m]
        y=B[0:n]
        x.extend(y)
        x.sort()
        A[0:m+n]=x
      
        
      

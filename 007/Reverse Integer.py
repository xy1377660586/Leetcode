class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            flag=-1
        a=str(abs(x))

        x = int(a[::-1])*flag
        
        if x < -(1 << 31) or x > (1 << 31) - 1:
            return 0
        else:
            
            return x

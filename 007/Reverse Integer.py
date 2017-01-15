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

        return int(a[::-1])*flag
                

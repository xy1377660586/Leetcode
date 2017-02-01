class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=1.0
        while abs(result*result-x)>0.1:
            result=(x+result*result)/(2*result)
        return int(result)
        %此题需要根据牛顿迭代法，见
        https://shenjie1993.gitbooks.io/leetcode-python/content/069%20Sqrt.html
        
       

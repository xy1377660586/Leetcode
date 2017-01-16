class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum=0
        maxdigit=1
        for i in range(len(s)-1,-1,-1):
            if digits[s[i]]>=maxdigit:
                maxdigit=digits[s[i]]
                sum+=digits[s[i]]
            else:
                sum-=digits[s[i]]
        return sum
    #思路见 http://blog.csdn.net/coder_orz/article/details/51448537

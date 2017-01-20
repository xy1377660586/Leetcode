class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)>len(haystack):
            return -1
        if len(needle)<=len(haystack):
            for i in range(len(haystack)):
                if haystack[i]==needle[0]:
                    index=i
                if len(haystack)>=i+len(needle) and haystack[i:i+len(needle)]==needle[0:len(needle)]:
                    return index
            return -1
a=Solution()
ss='weffsddvds'
ee='ffa'
print a.strStr(ss,ee)
#自己的写法，为什么在leetcode上报错

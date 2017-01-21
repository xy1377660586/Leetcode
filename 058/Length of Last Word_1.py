class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s[::-1]
        count=0
        j=0
        for i in range(len(s)):
            if s[i]!=' ':
                break
            j=j+1

        for i in range(j,len(s)):
            
            if s[i]==' ':
                break
            count+=1
        return count

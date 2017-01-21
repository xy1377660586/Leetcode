class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        oldstr='1'
        for i in range(n-1):
            tem=''
            count=1
            for j in range(1,len(oldstr)+1):
                if j<len(oldstr) and oldstr[j]==oldstr[j-1]:#如果还没到oldstr的最后一个字符而且当前字符等于前面一个字符
                    count+=1
                else:
                    tem+=str(count)+oldstr[j-1]实质上新的字符都是count和前一个不变的字符组成
                    count =1
            oldstr=tem 
        return oldstr
   题目的n 实际是从1开始读，一直把新得到的赋值给oldstr 继续读。

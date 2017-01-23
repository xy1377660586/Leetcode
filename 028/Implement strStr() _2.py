class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        lens=len(source)
        lent=len(target)
        for i in range (lens-lent+1):
            j=0
            while(j<lent):
                if source[i+j]!=target[j]:
                    break;
                j=j+1;
            if j==lent:
                return i
        return -1


class Solution:  
    # @return an integer  
    def reverse(self, x):  
        if 0 == x:  
            return 0  
        x = int(str(abs(x))[::-1]) * (x / abs(x))
        
        if x < -(1 << 31) or x > (1 << 31) - 1:#integer 应该注意边界问题！！,x d的边界需要满足范围 x > = -(31 << 1) and x < (1 << 31)-1
            return 0
        else:
            
            return x

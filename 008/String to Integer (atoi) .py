class Solution(object):
    # string转int，去首尾空格判读正负号，转换中注意Int范围
    def myAtoi(self, str):
        str = str.strip()
        if str == "" :
            return 0
        i = 0
        sign = 1
        ret = 0
        length = len(str)
        MaxInt = (1 << 31) - 1 #这里俄解释在下面俄链接里面可以看到:注意<<的优先级低于-
        if str[i] == '+':
            i += 1
        elif str[i] == '-' :
            i += 1
            sign = -1
        
        for i in range(i, length) :
            if str[i] < '0' or str[i] > '9' : #这个条件的作用呢? 为啥?是不是因为ascall表中的位置?
                break
            ret = ret * 10 + int(str[i])
            if ret > sys.maxint:#sys.maxint 是什么?需要导入import sys ,而? sys.maxint 的值是 9223372036854775807? 为什么是大于呢?
                break
        ret *= sign
        if ret >= MaxInt:
            return MaxInt
        if ret < MaxInt * -1 :
            return MaxInt * - 1 - 1 #补码表示的问题
        return ret
    
    
    #https://zhidao.baidu.com/question/176374554.html 关于取值范围的解释:
    #http://wenku.baidu.com/view/208bb2f20b4e767f5bcfceae.html?re=view

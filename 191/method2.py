class Solution(object):
	def hammingWeight(self, n):
		count=0
		while n:
			count+=n&1
			n>>=1#n 位移
		return count

	n>>=1是右移，相当于除以2，n&1相当于是位与操作。
	

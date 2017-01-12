n=11
class Solution(object):
	
	def hammingWeight(self, n,count):	
		yu=n%2
		ans=n/2
		if yu==1:
			count+=1	
		while ans!=0 and yu!=1:
			self.hammingWeight(ans)
		return count
count=0
a= Solution()
print a.hammingWeight(n,count)

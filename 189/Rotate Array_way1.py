nums=[1,2,3,4,5,6,7]
k=3
class Solution(object):
	def rotate(self, nums, k):
		
		length=len(nums)
		new=[0]*length
		for i in range(0,length):
			if i+k<length:
				new[i+k]=nums[i]
			if i+k>=length:
				new[i+(k-length)]=nums[i]
		return new

a=Solution()
print a.rotate(nums,k)为什么在python 里面编译通过，可是在LeetCode里面就出错啦？？

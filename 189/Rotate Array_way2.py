class Solution(object):
	def rotate(self, nums, k):
		
		n=len(nums)
		if n>1 and k>0:
			
			nums=nums[n-k :]+nums[: k]
		return nums
		if n==0:
			#return nums 这个语句不要啊因为不要求return anything
			
#
       

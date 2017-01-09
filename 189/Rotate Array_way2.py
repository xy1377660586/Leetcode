class Solution(object):
	def rotate(self, nums, k):
		
		n=len(nums)
		if n>1 and k>0:
			
			nums=nums[n-k :]+nums[: k]
		return nums
		if n==1:
		    return nums

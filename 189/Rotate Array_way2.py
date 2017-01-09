class Solution(object):
	def rotate(self, nums, k):
		
		n=len(nums)
		if n>1 and k>0:
			
			nums=nums[n-k :]+nums[: k]
		return nums
		if n==0:
			return nums
		
	#在LeetCode提交的时候报错！！！在python里面跑的时候么有！！！原因在于不要写return nums，可是why？？
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n - k:] + nums[:n - k]
       

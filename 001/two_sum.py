class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size=len(nums)
        for i in xrange(0,size):
            for j in xrange(i+1,size):
                
		if (nums[i]+nums[j]==target):
				return i,j

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        windows=[]
        if len(nums)<k:
           return False 
 
        while len(nums)==k:
            if nums[0]==nums[-1]: 报错奇葩
                return True
            
        for i in range(len(nums)-k):
            windows=nums[i+1:i+k+1] 
            if nums[i] in windows:
                return True
        return False

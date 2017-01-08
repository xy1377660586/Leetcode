class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if nums==[]:
            return 0
        index=0
        size=len(nums)
        for i in range(size):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
                
        return nums[:index]
        

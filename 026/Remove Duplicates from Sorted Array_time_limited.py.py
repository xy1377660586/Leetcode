class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums==[]:
            return 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i]==nums[i+1]:
                    del nums[i+1]
        return len(nums)
a=Solution()
nums = [1,1,1,2,3]   
c=a.removeDuplicates(nums)
print c

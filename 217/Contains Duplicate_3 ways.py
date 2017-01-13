方法一:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums) set()是删除列表里面的重复元素:
        
方法二: 此方法超时>>>自己写的......
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return False
        for i in range(0,len(nums)):
            print i
            for j in range(i+1,len(nums)):
               # print j
                if nums[j]==nums[i]:
                    return True
                
        return False
  方法三:
  class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                 return True

        return False 

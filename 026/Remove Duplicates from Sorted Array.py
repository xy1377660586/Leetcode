class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums==[]:
            return 0
        index=0  
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[index]:
                index+=1
                nums[index]=nums[i]# 数字不同就用index这个变量保存在原来的nums 的前几位，想删除重复的话只要把nums（：index）后面的删除就可以了
              
                
                
        
        
                
        return index+1

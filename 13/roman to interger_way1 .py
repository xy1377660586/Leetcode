class Solution:  
    # @return a boolean  
    def isPalindrome(self, x):  
        xx = x  
        new_xx = 0  
        while xx > 0:  
            new_xx = new_xx * 10 + xx % 10  
            xx /= 10  
  
        return new_xx == x 

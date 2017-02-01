class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
      

        if n<=2:
            return n
        dp=[0 for i in range(n)]
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n-1]        
动态规划（找规律的问题）
when i=1 2 3 4 8
  ways=1 2 3 5 8
  可见，从2 之后dp[i]=dp[i-1]+dp[i-2]
  

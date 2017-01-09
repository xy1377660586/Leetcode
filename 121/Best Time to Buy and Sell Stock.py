prices=[7, 1, 5, 3, 6, 4]
class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if prices==[]:
			return 0
		day=len(prices)
		min_value=min(prices)
		N=prices.index(min_value)
		if N==day-1:
			return 0
		for i in range(N+1,day):
			max_value=prices[i-1]
			if prices[i]>max_value:
				max_value=prices[i]
			profit=max_value-min_value
		return profit

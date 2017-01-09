prices=[7, 1, 5, 3, 6, 4]
class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		
		day=len(prices)
		if day<2:
			return 0
		maxprofit=0
		curMin=prices[0]
		for i in range(1,day):
			CurMin=min(CurMin,prices[i])
			maxprofit=max(maxprofit,prices[i]-CurMin)
		return maxprofit

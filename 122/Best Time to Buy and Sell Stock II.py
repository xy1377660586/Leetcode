class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if prices==[]:
			return 0
		day=len(prices)
		profit=0
		for i in range(1,day):
			if prices[i]-prices[i-1]>0:
				profit+=prices[i]-prices[i-1]
		return profit
    '''
    题目：用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。交易次数不限，但一次只能交易一支股票，也就是说手上最多只能持有一支股票
    ，求最大收益。

分析：贪心法。从前向后遍历数组，只要当天的价格高于前一天的价格，就算入收益。
    '''

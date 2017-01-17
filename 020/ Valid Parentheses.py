从左向右遍历字符串：

若为左括号则压入栈（append),若为右括号则将栈顶元素与该括号进行匹配，
若匹配则将该左括号出栈，若不匹配则直接返回假，遍历完成后如果栈为空则为正确括号序列，否则为不匹配括号序列
class Solution(object):
	def isValid(self, s):

		matchdir={'(':')','[':']','{':'}'}
		stacklist=[]
		for i in range(len(s)):
			if s[i] not in matchdir.keys() and len(stacklist)==0:
				return False
			elif s[i] in matchdir.keys():
				stacklist.append(s[i])
			elif s[i]==matchdir[stacklist[-1]]:
				stacklist.pop()
			else:
				return False
		if len(stacklist)==0:
			return True
		else:
			return False

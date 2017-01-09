# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#需要用一个help函数，当然也是递归的。当存在左右子树时，判断左右子树的根节点值是否相等，
#如果想等继续递归判断左子树根的右子树根节点和右子树根的左子树根节点以及左子树根的左子树根节点和右子树根的右子树根节点的值是否相等。
#然后一直递归判断下去就可以了
class Solution(object):
	def isSymmetric(self, root):
		if root:
			return self.help(root.right,root.left)
		return True

	def help(self,p,q):
		
		if p==None and q==None:
			return True
		if p and q and p.val == q.val:
			return self.help(q.left,p.right) and self.help(q.right, p.left)
		return False

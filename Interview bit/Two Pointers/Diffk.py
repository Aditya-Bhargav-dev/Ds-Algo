class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        d={}
        for i in A:
            diff=B+i
            if i in d:
                return 1
            else:
                d[diff]=1
        return 0

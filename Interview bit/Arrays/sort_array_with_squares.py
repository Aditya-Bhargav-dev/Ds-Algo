class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for i in range(0,len(A)):
            A[i]*=A[i]
        A.sort()
        return A

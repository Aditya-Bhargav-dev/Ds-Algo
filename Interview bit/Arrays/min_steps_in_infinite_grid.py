class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        x1 = A[0]
        y1 = B[0]
        minSteps = 0
        for i in range(1,len(A)):
            d = max(abs(A[i]-x1),abs(B[i]-y1))
            minSteps += d
            x1=A[i]
            y1=B[i]
        return minSteps

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i in range(len(A)-1):
            if i%2==0:
                if A[i]<A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
            else:
                if A[i]>A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
        return A
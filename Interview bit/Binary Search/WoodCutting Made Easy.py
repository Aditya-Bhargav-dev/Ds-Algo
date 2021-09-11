class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        minHeight = min(A)
        maxHeight = max(A)
        r = [i for i in range(minHeight,maxHeight+1)]
        l = 0
        h = len(r)-1
        w=-1
        while(l<=h):
            wood = 0
            mid = l+(h-l)//2
            for i in range(len(A)):
                if A[i]-r[mid]>0:
                    wood+=A[i]-r[mid]
            if wood<B:
                h=mid-1
            elif wood>B:
                l=mid+1
                w=r[mid]
            else:
                return r[mid]
        return w
                
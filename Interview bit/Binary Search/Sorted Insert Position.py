class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        l = 0
        h = len(A)-1
        if B>A[-1]:
            return h+1
        if B<A[0]:
            return 0
        while(l<=h):
            mid = l+(h-l)//2
            if B>A[mid]:
                l = mid+1
            elif B<A[mid]:
                h = mid-1
            else:
                return mid
        return l
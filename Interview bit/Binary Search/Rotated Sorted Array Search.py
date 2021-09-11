def binarySearch(A,B):
    l = 0
    h = len(A)-1
    while(l<=h):
        mid=l+(h-l)//2
        if A[mid]<B:
            l=mid+1
        elif A[mid]>B:
            h=mid-1
        else:
            return mid
    return -1
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        A=list(A)
        size = len(A)
        l = 0
        h = size-1
        while(l<h):
            mid=l+(h-l)//2
            if A[mid]>A[h]:
                l=mid+1
            else:
                h=mid
        index=size
        l-=1
        if l<0:
            l=size+l
        if B>=A[0] and B<=A[l]:
            index=binarySearch(A[:l+1],B)
        else:
            index=binarySearch(A[l+1:],B)
            if index!=-1:
                index+=l+1
        if index==size:
            return -1
        return index

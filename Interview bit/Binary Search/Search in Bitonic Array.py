def maxElement(A):
    l = 0
    h = len(A)-1
    while(l<h):
        mid = l+(h-l)//2

        if(A[mid] > A[mid+1]):
            h = mid
        else:
            l = mid+1
    
    return l

def binaryleftSearch(A,l,h,B):
    while(l<=h):
        mid = l+(h-l)//2
        if B>A[mid]:
            l=mid+1
        elif B<A[mid]:
            h=mid-1
        else:
            return mid
    return -1

def binaryrightSearch(A,l,h,B):
    while(l<=h):
        mid = l+(h-l)//2
        if B<A[mid]:
            l=mid+1
        elif B>A[mid]:
            h=mid-1
        else:
            return mid
    return -1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        m = maxElement(A)
        lFind = binaryleftSearch(A,0,m,B)
        rFind = binaryrightSearch(A,m+1,len(A)-1,B)
        if lFind!=-1:
            return lFind
        elif rFind!=-1:
            return rFind
        else:
            return -1
        

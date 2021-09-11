class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A)==1:
            if  A[0]>B:
                return 0
            else:
                return 1     
        l = 0
        h = len(A)-1
        count = -1
        index=-1
        while(l<=h):
            mid = l + (h-l)//2
            if B>A[mid]:
                l=mid+1
                count=max(mid,count)
            elif B<A[mid]:
                h=mid-1
            else:
                index=mid
                break
        if index==-1:
            return count+1
        count = 0
        x=index+1
        while(index>=0):
            count+=1
            index-=1
        while(x<len(A) and A[x]==B):
            count+=1
            x+=1
        return count 
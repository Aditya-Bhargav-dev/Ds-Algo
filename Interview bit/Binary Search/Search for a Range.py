class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if len(A)==1 and A[0]==B:
            return [0,0]
        l = 0
        h = len(A)-1
        index=-1
        while(l<=h):
            mid = l+(h-l)//2
            if B>A[mid]:
                l=mid+1
            elif B<A[mid]:
                h=mid-1
            else:
                index=mid
                break
        
        if index==-1:
            return [-1,-1]
        
        x=index+1
        while(index>=0 and A[index]==B):
            index-=1
        
        while(x<len(A) and A[x]==B):
            x+=1
 
        if x-1==index:
            return [index,index]
        else:
            return [index+1,x-1]
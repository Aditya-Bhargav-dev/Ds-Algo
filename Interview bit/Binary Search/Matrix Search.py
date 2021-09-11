class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        rangeMat=[]
        for i in A:
            if B>=i[0] and B<=i[-1]:
                rangeMat=i
                break
        if len(rangeMat)==0:
            return 0
        if len(rangeMat)==1 and B==rangeMat[0]:
            return 1
        l = 0
        h = len(rangeMat)-1
        while(l<=h):
            mid=l+(h-l)//2
            if B>rangeMat[mid]:
                l=mid+1
            elif B<rangeMat[mid]:
                h=mid-1
            else:
                return 1
        return 0
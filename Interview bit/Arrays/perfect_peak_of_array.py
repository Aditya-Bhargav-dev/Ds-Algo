class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        leftMax = [0]*len(A)
        rightMin = [0]*len(A)
        leftMax[0]=A[0]
        rightMin[-1]=A[-1]
        for i in range(1,len(A)):
            leftMax[i]=max(A[i],leftMax[i-1])
        
        for i in range(len(A)-2,-1,-1):
            rightMin[i]=min(A[i],rightMin[i+1])
        
        for i in range(1,len(A)-1):
            if A[i]>leftMax[i-1] and A[i]<rightMin[i+1]:
                return 1
        return 0
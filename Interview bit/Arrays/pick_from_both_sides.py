class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        currSum = sum(A[:B])
        j=len(A)-1
        maxSum = currSum
        i=B-1
        while(i>=0 and j>=0):  
            currSum+=A[j]
            currSum-=A[i]          
            j-=1
            i-=1
            maxSum=max(currSum,maxSum)
 
        return(maxSum)

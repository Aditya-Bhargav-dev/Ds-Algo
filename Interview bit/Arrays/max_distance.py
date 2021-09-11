class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not A:
            return -1
        N = len(A)
        leftMin = [0]* N
        rightMax = [0] * N
 
        rightMax[N-1] = A[N-1]
        for i in range(N-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], A[i])
        
        leftMin[0] = A[0]
        for i in range(1, N):
            leftMin[i] = min(leftMin[i-1], A[i])
        
        minI = maxJ = 0
        currMax = 0
        while minI < N and maxJ < N:
            if leftMin[minI] <= rightMax[maxJ]:
                currMax = max(currMax, maxJ - minI)
                maxJ += 1
            else:
                minI += 1
        
        return currMax
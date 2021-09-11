class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        maxNum = max(A)
        if maxNum <=0:
            return 1
        A.sort()
        positives={}
        for i in A:
            if i not in positives and i>0:
                positives[i]=1
        for i in range(1,maxNum):
            if i not in positives:
                return i
        return maxNum+1
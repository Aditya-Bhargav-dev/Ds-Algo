class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A < 0:
            return []
        pascal = [[1]]
        if A == 0:
            return pascal[0]
        for i in range(0,A):
            l=[1]
            for j in range(1,len(pascal[i])):
                l.append(pascal[i][j]+pascal[i][j-1])
            l.append(1)
            pascal.append(l)
        return pascal[-1]
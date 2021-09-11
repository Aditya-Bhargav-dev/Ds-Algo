class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        sumOfList = sum(A)
        n = len(A)
        sumOfRange = int(n * (n + 1) / 2) - n
        return sumOfList - sumOfRange

#2nd method
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        freq = {}
        for i in A:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for k,v in freq.items():
            if v>1:
                return k
 
        return -1
 
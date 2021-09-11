class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        freq = {}
        ans = []
        n = len(A)
        for i in A:
            if i in freq:
                ans.append(i)
                break
            else:
                freq[i]=1
        totalSum = sum(A)
        sumOfN = n * (n+1) // 2
        ans.append(sumOfN - totalSum + ans[0])
        return ans
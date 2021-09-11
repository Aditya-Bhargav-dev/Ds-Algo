class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pre = []
        post = [0]*len(A)
        val = 0
        for i in range(len(A)):
            if i % 2 == 0:
                val  += A[i]
            else:
                val -=  A[i]
            pre.append(val)
            
        val  = 0
        for i in range(len(A) - 1, -1, -1):
            if i % 2 == 0:
                val += A[i]
            else:
                val -= A[i]
            post[i] = val
            
        count = 0
        for i in range(0, len(A)):
            if pre[i] == post[i]:
                count += 1
                
        return count
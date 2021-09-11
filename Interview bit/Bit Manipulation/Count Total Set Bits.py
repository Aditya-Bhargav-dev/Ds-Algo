class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if (A==0):
            return 0
        t=A+1
        i=2
        count =0
        while(i<=2*(t-1)):
            count+=(t/x)*x/2
            if ((t%x)>x/2):
                count+=(t%x)-(x/2)
            i*=2
        
        return count%1000000007

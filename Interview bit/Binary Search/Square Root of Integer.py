import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==0:
            return 0
        if A==1:
            return 1
        l=1
        h=A//2
        while(l<=h):
            mid=l+(h-l+1)//2
            sq = mid*mid
            if sq==A:
                return math.floor(mid)
            if sq>A:
                h=mid-1
            else:
                l=mid+1
        return math.floor(h)
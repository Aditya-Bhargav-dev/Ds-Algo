class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):   
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x % d
        if n % 2 == 0:
            half = self.pow(x, n//2, d)
            return (half * half) % d  
        else:
            half = self.pow(x, (n-1) // 2, d)
            return (half * half * x) % d
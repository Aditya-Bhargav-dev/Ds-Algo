from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if not A:
            return 0
        
        def compare(n1, n2):
            if int(n1+n2)>int(n2+n1):
                return -1
            else:
                return 1
        
        nums = list(map(str, A))
        nums.sort(key=cmp_to_key(compare))
        return str(int(''.join(nums)))
from itertools import permutations
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ['a','e','i','o','u']
        vowCount = 0
        consCount = 0 
        c=0
        for i in A:
            if i in vowels:
                vowCount+=1
            else:
                consCount+=1
        for i in A:
            if i in vowels:
                c+=consCount%1000000007
                vowCount-=1
            else:
                c+=vowCount%1000000007
                consCount-=1

            
        return c%1000000007



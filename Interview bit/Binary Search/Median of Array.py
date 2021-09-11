class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        l = 0
        a= len(A)
        b = len(B)
        h=a
        
        while(l <= h):
            position_a = (l+h)//2
            position_b = (a + b + 1)//2 - position_a
            
            max_left_a = float('-inf') if position_a == 0 else A[position_a -1]
            min_right_a = float('inf') if position_a == a else A[position_a]
            
            
            max_left_b = float('-inf') if position_b == 0 else B[position_b -1]
            min_right_b = float('inf') if position_b == b else B[position_b]
            
            if (max_left_a <= min_right_b and max_left_b <= min_right_a):
                if (a+b)%2 == 0:
                    return float(max(max_left_a ,max_left_b) + min(min_right_a , min_right_b))/2
                else:
                    return max(max_left_a,max_left_b)
                    
            elif max_left_a > min_right_b:
                h = position_a -1 
            else:
                l = position_a + 1





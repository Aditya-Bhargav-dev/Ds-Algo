def isValid(C,A,m):
    p=1
    paintSum = 0
    for i in C:
        if paintSum+i<=m:
            paintSum+=i
        else:
            p+=1
            paintSum=i
        if p>A:
            return False
    return True
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def paint(self, A, B, C):
        for i in range(len(C)):
            C[i]*=B
        l = len(C)
        m=max(C)
        ans=-1
        if A>l:
            return m
        else:
            start = m
            end = sum(C)
            while(start<=end):
                mid = start+(end-start)//2
                if isValid(C,A,mid):
                    ans=mid
                    end = mid-1
                else:
                    start = mid+1
        return ans%10000003




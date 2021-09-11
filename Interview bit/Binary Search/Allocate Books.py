def isValid(A,B,maxPages,totalPages):
    s=1
    pageSum = 0
    for i in A:
        if pageSum+i<=maxPages and pageSum+i<totalPages :
            pageSum+=i
        else:
            s+=1
            pageSum=i
        if s>B:
            return False
    return s<=B
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        l=len(A)
        m=max(A)
        ans=-1
        if B>l:
            return -1
        elif B==l:
            return m
        elif B==1:
            return sum(A)
        else:
            start = m
            end = sum(A)
            totalPages = end
            while(start<=end):
                mid = start+(end-start)//2
                if isValid(A,B,mid,totalPages):
                    ans=mid
                    end = mid-1
                else:
                    start = mid+1
        return ans
        

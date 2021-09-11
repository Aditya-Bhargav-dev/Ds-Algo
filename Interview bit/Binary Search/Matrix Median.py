class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        freq = {}
        for i in A:
            for j in i:
                if j in freq:
                    freq[j]+=1
                else:
                    freq[j]=1
        full = []
        for k,v in sorted(freq.items()):
            for i in range(v):
                full.append(k)
        l=len(full)
        if l%2!=0:
            return full[l//2]
        else:
            return (full[l//2 -1]+full[l//2])/2
 
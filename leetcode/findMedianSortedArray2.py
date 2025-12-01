
def median(a):
    return int(a/2 + 0.5)
def part(A,B,m1,m2,m,n):
    if m1 == m:
        return B[median(m2-1)]
    if m2 == 0:
        return A[median(m1+1)]
    
    if A[m1] == B[m2]:
        return A[m1]    
    elif A[m1] < B[m2]:
        return part(A,B,median(m1+m),median(n-m2),median(m),median(n))
    else:
        return part(B,A,median(m2+n),median(m-m1),median(n),median(m))

def findMedianSortedArray(nums1,nums2):
    m, n = len(nums1)-1, len(nums2)-1
    m1, m2 = median(m), median(n)
    if m<=n:
        return part(nums1,nums2,m1,m2,m,n)
    else:
        return part(nums2,nums1,m2,m1,n,m)

print(findMedianSortedArray([1,2,3,4,5],[6,7,8,9,10,11,12,13,14,15,16,17]))


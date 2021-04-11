nums1=[1,2,3]
nums2=[4,5,6]
i = nums1 + nums2 
i.sort(reverse = False)
print(i)
k = len(i)
print(k)
if (k % 2) == 0:
    idx1 = k/2
    idx2 = (k-2)/2
    print(idx1,idx2)
    print((i[idx1]+i[idx2])/2)
else:
    idx = (k-1)/2
    print(i[idx])
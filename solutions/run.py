#two scenario, odd or even 
"""
odd: average
even: take the one
"""
nums1=[1,3]
nums2=[2]


def findMedianSortedArrays( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    fulllen=len(nums1)+len(nums2)
    if fulllen==0: 
        return 0
    elif fulllen<=2: 
        return(sum(nums1+nums2)/fulllen)
    toendi=fulllen/2
    result,l,r=0,-1,-1

    if toendi!=toendi//1: 
        #odd
        toendi=int(toendi//1)
        if not nums1: return(nums2[toendi])
        if not nums2: return(nums1[toendi])
        for i in range(toendi+1): 
            takeresult=True if i== toendi else False#last iterate
            if ((r>=0)&(r+1 == len(nums2)))|(nums1[l+1]<nums2[r+1]):
                l+=1
                result=nums1[l] if takeresult else 0
            else: #((l>=0)&(l+1==len(nums1))) or  nums1[l+1]>nums2[r+1]
                r+=1
                result=nums2[r] if takeresult else 0

    else:
        #even
        toendi=int(toendi)
        if not nums1: return((nums2[toendi]+nums2[toendi-1])/2)
        if not nums2: return((nums1[toendi]+nums1[toendi-1])/2)
        for i in range(toendi+1): 
            #take the result for the first and senond one
            takeresult=True if (i== toendi)|(i== toendi-1) else False
            if ((r>=0)&(r+1 == len(nums2)))|(nums1[l+1]<nums2[r+1]):
                l+=1
                result=result+nums1[l] if takeresult else result
            else: #l+1==len(nums1) or  nums1[l+1]>nums2[r+1]
                r+=1
                result=result+nums2[r] if takeresult else result
        #take average
        result=result/2
    return result


print(findMedianSortedArrays( nums1, nums2))
stop

fulllen=len(nums1)+len(nums2)
#if fulllen==0: 
    #return 0
#elif fulllen<=2: 
    #return(sum(nums1+nums2)/fulllen)
toendi=fulllen/2
result,l,r=0,-1,-1

if toendi!=toendi//1: 
    #odd
    toendi=int(toendi//1)
    if not nums1: print(nums2[toendi])
    if not nums2: print(nums1[toendi])
    for i in range(toendi+1): 
        takeresult=True if i== toendi else False#last iterate
        if ((r>=0)&(r+1 == len(nums2)))|(nums1[l+1]<nums2[r+1]):
            l+=1
            result=nums1[l] if takeresult else 0
        else: #((l>=0)&(l+1==len(nums1))) or  nums1[l+1]>nums2[r+1]
            r+=1
            result=nums2[r] if takeresult else 0

else:
    #even
    toendi=int(toendi)
    if not nums1: print((nums2[toendi]+nums2[toendi-1])/2)
    if not nums2: print((nums1[toendi]+nums1[toendi-1])/2)
    for i in range(toendi+1): 
        #take the result for the first and senond one
        takeresult=True if (i== toendi)|(i== toendi-1) else False
        if ((r>=0)&(r+1 == len(nums2)))|(nums1[l+1]<nums2[r+1]):
            l+=1
            result=result+nums1[l] if takeresult else result
        else: #l+1==len(nums1) or  nums1[l+1]>nums2[r+1]
            r+=1
            result=result+nums2[r] if takeresult else result
    #take average
    result=result/2
print(result)
stop


if toendi!=toendi//1: 
    #even
    toendi=int(toendi//1)
    if not nums1: print(nums2[toendi])
    if not nums2: print(nums1[toendi])
    for i in range(toendi+1): 
        takeresult=True if i== toendi else False#last iterate
        if r+1 == len(nums2):
            l+=1
            result=nums1[l] if takeresult else 0
        elif l+1==len(nums1):
            r+=1
            result=nums2[r] if takeresult else 0
        elif nums1[l+1]>nums2[r+1]:
            r+=1
            result=nums2[r] if takeresult else 0
        else:
            l+=1
            result=nums1[l] if takeresult else 0

else:
    #odd
    if not nums1: print((nums2[toendi]+nums2[toendi+1])/2)
    if not nums2: print((nums1[toendi]+nums1[toendi+1])/2)

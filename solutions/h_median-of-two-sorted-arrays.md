# Question
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
```

# initial solutions:

## S1:without creating another list
```python
class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
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
            print(result)

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
```

## s2:class Solution(object):

```python
    def findMedianSortedArrays(self,nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=sorted(nums1+nums2)
        #nums1.append(nums2)
        toendi=len(nums1)/2
        if toendi==0:
            raise ValueError
        if toendi!=toendi//1: #odd
            return nums1[int(toendi//1)]
        else: #even
            return (nums1[int(toendi)]+nums1[int(toendi)-1])/2

```

# explanation

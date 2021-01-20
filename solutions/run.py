def threeSum( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    i=0
    result=list()
    if len(nums)<3:return result
    nums=sorted(nums,reverse=True)
    while (len(nums)>=3)&(i<len(nums)-2) &(nums[i]!=0):
        #stop until the nums is through or until 0
        l=i+1
        r=len(nums)-1
        while r>l: #try to make nums[i] to 0
            if nums[i]+nums[r]+nums[l]==0:
                if [nums[i],nums[l],nums[r]] not in result: 
                    result+=[[nums[i],nums[l],nums[r]]]
                l+=1
            elif nums[i]+nums[r]+nums[l]>0:
                l+=1
            else:
                r-=1
        i+=1
    if nums.count(0)>=3: result=result+[[0,0,0]]
    return result

final=threeSum([-1,0,1,0])
                    
print('i')
def plusOne(digits):  # O(n) both
    i,carry=1,1
    while (carry==1) & (i<=len(digits)):
        print(digits[-i]+carry)
        if digits[-i]+carry == 10:
            digits[-i]=0
            i+=1
        else:
            digits[-i]+=1
            carry=0
            
        if (carry==1) &(i==len(digits)+1):
            digits=[1]+digits
            i+=1
    return digits

plusOne([9])
print(1)
print('i')
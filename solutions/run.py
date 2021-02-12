ls = list()
nums = [1, 2, 1, 3, 3]

while nums:
    num = nums[0]
    count = 0
    while num in nums:
        nums.remove(num)
        count = count + 1
    if count == 1: print(num) 
        

for i in range(len(nums)):
    for j in range(len(nums)):
        1+1







for num in nums:
    if num not in ls:
        nums.remove(num)
    else:
        ls = ls + [num]
print(ls.pop())

        

print('hi')
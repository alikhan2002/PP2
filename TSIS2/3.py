nums = [1,2,3,1,1,3]
n=len(nums)
cnt=0
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] == nums[j]: cnt += 1
    
print(cnt)
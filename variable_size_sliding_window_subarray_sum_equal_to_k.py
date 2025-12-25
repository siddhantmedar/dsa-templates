#Variable size sliding window

nums = [4, 1, 1, 1, 2, 3, 5]
target = 5

i,j = 0, 0 #ptrs

sum, sidx, eidx, length = 0, 0, 0, 0

while j<len(nums):
    if sum == target:
        if ((j-1)-i+1) > length:
            length = max(length, (j-i))
            sidx = i
            eidx = j-1
        sum+=nums[j]
        j+=1
    elif sum < target:
        sum+=nums[j]
        j+=1
    elif sum > target:
        while sum > target and i < len(nums):
            sum-=nums[i]
            i += 1

print(nums[sidx:eidx+1])
print(length)

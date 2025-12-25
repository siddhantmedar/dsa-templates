from collections import deque

nums = [12,-1,-7,8,-15,30,16,28]
k = 3

res = []
q = deque()

#build a window of size k
for i in range(k):
    if nums[i] < 0:
        q.append(nums[i])

res.append(q[0])
#move forward with size k window

for i in range(k, len(nums)):
    if q[0] == nums[i-k]:
        q.popleft()
    if nums[i] < 0:
        q.append(nums[i])

    if q:
        res.append(q[0])
    else:
        res.append(0)
        
print(res)
#nums = [3,2,1,2,1,7]
nums = list(map(int,input().split(",")))
print(nums)




nums = list(map(int,input().split(",")))
count= 0
new_nums = []
for j in range(len(nums)):
    while 1:
        if nums[j] not in new_nums:
            new_nums.append(nums[j])
            break
        else:
            nums[j] += 1
            count += 1
print(count)




nums = [-1,-3,4,7]

def selection_sort(nums):
    position = -1
    tem = -1

    for i in range(len(nums)):
        position = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[position]:
                position = j
        nums[i],nums[position] = nums[position],nums[i]

selection_sort(nums)
print(nums)

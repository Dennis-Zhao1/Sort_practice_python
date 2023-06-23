import random

def quick_sort(nums,low,high):
    if low < high:
        pivot_index = pivot_partion(nums,low,high)
        quick_sort(nums,low,pivot_index-1)
        quick_sort(nums,pivot_index+1,high)
    
def pivot_partion(nums,low,high):
       
    # using two pointers, i store the final position, means all the numbers that in the left side of i are smaller than pivot.
    i = low
    # j is the other pointer, means all the numbers that in the right side of j are larger than pivot.
    j = high - 1

    while i < j:  # i < j means has finished this loop, in this loop, all numbers in the left side of i are smaller, and in the right side of j are larger, and i is the final position of pivot
        # if nums[i] smaller than pivot, than do nothing, just move i to next
        if nums[i] < nums[high]:
            i += 1
        # if nums[i] larger than pivot, than swaps nums[i] and nums[j], and j--    
        else:
            nums[i],nums[j] = nums[j],nums[i]
            j -= 1
    # now put pivot to the final position i.
    nums[i],nums[high] = nums[high],nums[i]
    # return final position i
    return i


nums = [1,9,8,5,3]
print(nums)
quick_sort(nums,0,len(nums)-1)    
print(nums)

nums1 = [1, 7, 4, 1, 10, 9, -2]
print(nums1)
quick_sort(nums1,0,len(nums1)-1)    
print(nums1)
    



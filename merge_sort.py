nums = [1,3,5,7,9,8,0,6,4,2]

def merge_sort(nums,left,right):
    
    def combion(left,right):
        combioned = []
        i = 0
        j = 0
        # combioned append the smaller one
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                combioned.append(left[i])
                # print(f"combioned is {combioned}")
                i += 1
            else:
                combioned.append(right[j])
                # print(f"combioned is {combioned}")
                j += 1

        # if right has done
        while i < len(left):
            combioned.append(left[i])
            # print(f"combioned is {combioned}")
            i += 1
        # if left has done
        while j < len(right):
            combioned.append(right[j])
            # print(f"combioned is {combioned}")
            j += 1
        return combioned


    solution = []
    # base case
    if left == right:
        solution.append(nums[left])
        return solution

    mid = (left + right) // 2
    # recurtion left and right
    solu_left = merge_sort(nums,left,mid)
    print(solu_left)
    solu_right = merge_sort(nums,mid+1,right)
    print(solu_right)

    solution = combion(solu_left,solu_right)
    return solution
    
    


new_nums = merge_sort(nums,0,9)
print(new_nums)
#  A1B2C3D4  ->  1234ABCD

my_lsit = ['A','1','B','2','C','3','D','4']

def merge_sort_ex(arr,left,right):
    def combion(left,right):
        combioned = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                combioned.append(left[i])
                i += 1
            else:
                combioned.append(right[j])
                j += 1
        while i < len(left):
            combioned.append(left[i])
            i += 1
        while j < len(right):
            combioned.append(right[j])
            j += 1        
        
        return combioned

    solution = []
    # base case
    if left == right:
        solution.append(arr[left])
        return solution

    mid = (left + right) // 2
    # recurtion left and right
    solu_left = merge_sort_ex(arr,left,mid)
    print(solu_left)
    solu_right = merge_sort_ex(arr,mid+1,right)
    print(solu_right)

    solution = combion(solu_left,solu_right)
    return solution

result = merge_sort_ex(my_lsit,0,len(my_lsit)-1)
print(result)
print('A'<'1')
# Given an array stored in stack1, how to sort the numbers by using additional two stacks?
# Follow up, what if only 1 additional stack can be used?

stack1 = [-1,-3,4,7]


def stack_simulate_sort(stack):
   
    stack2 = []
    stack3 = []
    while not len(stack) == 0:
        global_min = stack[len(stack)-1]
        # this loop pop stack,and find the global_min, then store all items in stack2
        for i in range(len(stack)):
            cur = stack.pop()           
            if global_min > cur:
                global_min = cur
            stack2.append(cur)        

        # this loop pop stack2, if equal to global_min, store in stack3, else store in stack
        for i in range(len(stack2)):
            curr = stack2.pop()
            if global_min == curr:
                stack3.append(curr)
            else:
                stack.append(curr)
        

stack_simulate_sort(stack1)
print(stack1)

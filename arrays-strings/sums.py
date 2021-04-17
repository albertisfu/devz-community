
# Alberto Islas 
# Given an array of numbers and a target number, check if the target number can be produced by the sum of two elements contained in the array, return the indices of two elements if found


def find_sum(array, target):
    array_len = len(array)
    for i in range(array_len):
    
        to_find = target - array[i]


        val = array.index(to_find) if to_find in array else None

    
        if val !=None:
            return [i, val]
        

nums = [2,1,5,7]
target = 9

nums1 = [3, -1, 0, 1]
target1=0


sum_index = find_sum(nums, target)

print(sum_index)

print('------------------')

sum_index1 = find_sum(nums1, target1)

print(sum_index1)

nums_test = [2, 7, 11, 15]
target_test = 9

def twoSum(nums, target):
    twoSumExist = False
    present_number_index = 0
    for i in nums:
        inner_index = 0
        for next in nums:
            if present_number_index == inner_index:
                inner_index += 1
                continue
            else :
                if target == next + i:
                    twoSumExist = True
                    return print(present_number_index, inner_index, twoSumExist)
                    
                else:
                    inner_index += 1
                    continue
        present_number_index += 1 

twoSum(nums_test,target_test)  
   

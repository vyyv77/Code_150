nums_test = [1,2,3,4]
result_test = [24,12,8,6]


def productExcepySelf(nums):
    outer_index = 0
    results =[]
    for curr in nums:
        inner_index = 0
        result_num = 1
        for i in nums:
            if outer_index != inner_index:
                result_num *= i
                inner_index += 1
                
            else:
                inner_index += 1
                continue
        results.append(result_num)
                
        outer_index += 1
    return results



result_list = productExcepySelf(nums_test)
print(result_list)


nums_test = [1,  2, 3,3,3,3,3, 4,4,4,8]
k_test = 2

def topKFrequent(nums, k):
    number_checked = []
    number_checked_frequency =[]
    current_index = 0
    for i in nums:
        if i not in number_checked:
            number_checked.append(i)
            inner_index = 0
            current_num_checked_frequency = 0
            for n in nums:
                #print(inner_index)
                if inner_index != current_index:
                    if i == n :
                        current_num_checked_frequency += 1
                        inner_index += 1
            
                    else :
                        inner_index += 1
                        continue
                else :
                    current_num_checked_frequency += 1
                    inner_index += 1
            number_checked_frequency.append(current_num_checked_frequency)
            current_index += 1
        else:
            current_index += 1
            continue
    max_entries = []
    while k != 0:
        print(max_entries)
        index_of_max_frequency = number_checked_frequency.index(max(number_checked_frequency))
        number_to_append = number_checked[index_of_max_frequency]
        

        print(number_checked_frequency)
        print(number_checked)
        number_checked_frequency.pop(index_of_max_frequency)
        number_popped = number_checked.pop(index_of_max_frequency)
        print("num_pop : ", number_popped)
        max_entries.append(number_to_append)
        
        k -= 1
    return max_entries

new_list = topKFrequent(nums_test, k_test)
print(new_list)
#new_list = topKFrequent(nums_test, k_test)
#print(new_list)
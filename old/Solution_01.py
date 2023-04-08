test = [1, 2, 4, 6, 6]

#for x in range(0, len(test)):
#    print(test[x])



def main(nums):

    
    for curr in nums:
        occurence = 0
        start = 0
        end = len(nums)
        for x in range(start,end):
            print(curr, nums[x])
            if curr == nums[x]:
                occurence += 1
            if occurence > 1:
                return True
        start += 1
    return False

if __name__ == "__main__":
    result = main(test)
    print(result)
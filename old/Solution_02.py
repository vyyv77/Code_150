# ==>variable is declared outside the loop if we want to transfer knowledge gained 
# from inside loop to outside

#  ==>sometimes starting info for each outer loop is same that is why "locationCurrent"
# isalways 0 as for key that key should be searched from first location in second list
# if we put locationCurrent inside inner loop outer loop will get start from the first letter modified to 8

# ==> else if we want to just change or modify the thing we are looping we declare 
# the variable inside or when info is not meant to be sent outside loop



first = "anagram"

second = "ganaram"
first_list = list(first)
second_list = list(second)

def isAnagram(s, t):

    if len(s) == len(t):
        allKeysFound = False
        for key in s:    
            isKeyThere = False
            locationCurrent = 0
            for curr in t:
                
                if curr != '8':
                    print("checked for : ", key, " : ", curr)
                    if key == curr:
                        isKeyThere = True
                        t[locationCurrent] = '8'
                        print("second word : ", t)
                        locationCurrent += 1
                        break
                    else:
                        locationCurrent += 1
                        continue
                else :
                    locationCurrent += 1
                    continue
            if isKeyThere == True:
                print(isKeyThere , key)
                allKeysFound = True
                continue
            else:
                allKeysFound = False
                return allKeysFound
        return allKeysFound
    else:
        return False

result = isAnagram(first_list, second_list)
print(result)

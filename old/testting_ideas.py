var = "myname"
new_var = list(var)
print(new_var)
curr_location = 0
for curr in new_var:
    if curr == 'e':
        new_var[curr_location] = '8'
    curr_location += 1

print(new_var)
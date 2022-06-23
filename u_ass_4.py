list1 = [1,2,2,7,9,9,8,5,3]
flag = False
sum = 0
for i in range (len(list1)):
    if list1[i]==7:
        flag = True
    if flag == False:
        sum = sum + list1[i]
    if list1[i]==8:
        flag = False
print(sum)

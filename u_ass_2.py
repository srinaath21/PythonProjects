def last2(str):
    count = 0
    temp = str[-2:]
    print("temp = ",temp)
    for i in range(len(str)-2):
        sub = str[i : i+2]
        print("sub = ", sub)
        if sub == temp:
            count+=1
        return count 
word = input()
print(last2(word))
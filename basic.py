one = []
n = int(input())
m = int(input())
for i in range (m):
    one.append(1)
print(one)
for i in range(len(one)-1):
    if (i)%2==0:
        one.insert(i+1, 0)
print(one)
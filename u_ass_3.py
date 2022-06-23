word1 = input()
word2 = input()
count = 0
short_word = min(len(word1),len(word2))
for i in range(short_word-1):
    if(word1[i:i+2] == word2[i:i+2]):
        count+=1
print(count)
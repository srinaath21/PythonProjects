def sen_maker(phrase):
    if phrase.startswith(("how", "when", "where", "who", "what")):
        print(phrase.capitalize() + '? ',end='')
    else:
        print(phrase.capitalize() + '. ',end='')
str = []
while True:
    n = input("Say something: ")
    if n =='\end':
        break
    else:
        str.append(n)
        continue
for i in str:
    sen_maker(i)
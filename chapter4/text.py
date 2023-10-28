names = [ "Bob", "Jack", "Rob", "Bob", "Robert" ]
for i in names:
    if names.count(i) > 1:
        names.remove(i)
print(names)

name_list = []
while True:
    v = input('enter a name or write quit to stop: ')
    if v == 'quit':
        for i in name_list:
            print(i,end=',')
        break
    name_list.append(v)

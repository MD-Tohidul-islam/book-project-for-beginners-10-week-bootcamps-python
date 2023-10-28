#  import additional fuctions
import random
#from IPython.display import clear_output
words = ['tree','basket','chair','paper','python']
v = random.choices(words)
b1 = str(v[0])
c=''
for i in v:
    c+=i
print(c)
n= len(c)
b=['-']*len(c)
while n>0:
    user_guess = input('enter a letter: ')
    #count1 = c.count(user_guess)
    if user_guess in c:
        if user_guess not in b:
            b[c.index(user_guess)] = user_guess
            c = list(c)
        else:
            l = [i for i , j in enumerate(c) if j == user_guess]
            b[l[0]] = user_guess
        c[c.index(user_guess)] = ' '
        #print(user_guess, 'is', count1, 'times in name')

    else:
        print('wrong guess')
    x = ''
    for j in b:
        x += j
    n -= 1
    if x == b1:
        print('you guess right , you win')
    else:
        print(x, n,'guess left')













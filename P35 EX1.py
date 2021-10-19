num=int(input('plz insert a num'))
i=0
for i in range(1, 100, 1):
    num2= int(input('Plz insert a number'))
    if num>num2:
        print('the numbers are NOT SORTED')
        break
    num=num2
    i+=1
if i==100:
    print('the number are SORTED')



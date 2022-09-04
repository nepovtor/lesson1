a = int(input('Введите число '))
b = int(input('Введите число '))
c = int(input('Введите число '))
print('a =',a,' b =',b,' c =',c)
if(a<b+c)and(b<a+c)and(c<a+b):
    print('yes')
else:
    print('no')

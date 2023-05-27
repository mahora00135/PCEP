i = input("Pleas enter a number:")
i = int(i)
#print(i)
print(type(i))
j = input('Pleas enter another number;')
j = int(j)
#print(i + j)
k = input('pleas enter a operation(/, - , + , *):')

if k == "-" :
    print(i-j)
elif k == "+" : 
    print(i + j)
elif k == "*" :
    print(i *j)
elif k == "/" and j != 0:
    print(i/j)
else:
    print('not a valid operation.')
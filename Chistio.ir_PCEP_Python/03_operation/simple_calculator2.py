i = input("Pleas enter a number:")
i = int(i)
#print(i)
print(type(i))
j = input('Pleas enter another number;')
j = int(j)
#print(i + j)

k = input('pleas enter a operation(/, - , + , *):')
valid_operations = ['-', '+', '/', '*' ]
if k in valid_operations :
    print('valid operation')
else:
    print('not a valid operation')
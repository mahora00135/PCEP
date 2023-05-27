'''
our_list = [4, 5, 1, 9, 0, 10]
for l in our_list:
    print(l)
    #if l > 5:
    #    print(l)
print('done')
'''

'''
i = 1
while i < 10:
    print(i)
    i = i + 1
print('done')
'''

'''
i = 1
while i < 10:
    print(i)
print('done')
'''

i = 0
sum = 0
count = 0
while i != '':
    i = input('Please enter a number (left blank to calculate mean):')
    if i == '':
        continue
    i = int(i)
    sum = sum +i
    count = count + 1 

print(sum / count)
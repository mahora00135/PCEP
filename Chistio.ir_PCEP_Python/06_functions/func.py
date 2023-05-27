def search_customers(x):
    customers = ['09121234','09131234','09111234','09101234']
    if x in customers:
        return True
        #return 10
    else:
        return False
        #return 20
    
    
    
    

i = input('please enter a phone number:')
result = search_customers(i)
#if result == 10
if result:
    print('yes, The customer exists')
#elif result == 20
else:
    print('No, The customer dose not exist')


result = search_customers('09121234')
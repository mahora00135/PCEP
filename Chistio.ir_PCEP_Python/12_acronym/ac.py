def user_input():
    i = input('pleas enter a phrase: ')
    return i
def acronym(i):
    j = i.split()
    k = []
    for word in j :
        if len(word) <= 2 :
            continue
        k.append(word[0])
    s = ""
    s = s.join(k)
    return s


ui = user_input()
a = acronym(ui)
print(a)
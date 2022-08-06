def numberof_words(string):
    count = 0
    for i in string:
        if i == ' ':
            count = count+1
    return count
a = numberof_words('I AM A GOOD BOY')
print(a)
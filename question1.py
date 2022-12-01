
a = ['great', 'abc', 'hello','hiyo']
for i in range (len(a)):
    for j in range (i+1, len(a)):
        if a[i][-2] > a[j][-2]:
            a[i],a[j] = a[j],a[i]
print(a)  
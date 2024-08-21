a = [2,6,4,8,7,9]

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
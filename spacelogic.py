print(chr(32))

a = input("this is list: ")

arr = list(a)

print(arr)

res = []

for ele in arr:
    j = ele.replace(' ','22')
    res.append(j)
    
print(res)


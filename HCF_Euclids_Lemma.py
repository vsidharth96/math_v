
k=[]
for i in range(1,100):
    for j in range(2,i):

        if i%j==0:
            #print(i," is a composite")
            break
    else:
        #print(i," is a prime")
        k.append(i)

print(k)
print(min(k))
print(max(k))









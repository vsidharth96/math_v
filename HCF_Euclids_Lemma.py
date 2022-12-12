# To find the if a number is prime or composite , and to find the nearest prime number within the limit

a= int(input("Please enter a number : ")) #Input a number
k=[] #open an empty list to store all the composite numbers

for i in range(1,a+1): #initialise for loop to iterate from 1 to the said number
    for j in range(2,i): #initialise a second for loop to iterate from 2 to current number
        if i%j==0: #conditional operation to check if the modulus is zero
            break
    else: #else out of if as we have a break statement to proceed if there is a break
        k.append(i) #add values to the list

if max(k)==a: #conditional statement to check the last value in the K list is equal to our given value as it must stop in the last number
    print(a,"is Prime")
    print(len(k)," prime numbers are there within the limit")
else:
    print(a,"is Composite")
    print(k[-1]," is the nearest prime within the limit") #else print the last prime number in the list
    print(len(k)," prime numbers are there within the limit") #print the total numbers in the list









num_1 = int(input("Enter a number: "))
print ('Thank you!' if 1 < num_1 < 10**25 else 'Please, choose another number') 

n = 0
for i in range(num_1+1):
    n += i
print("The sum of these numbers:", n)    

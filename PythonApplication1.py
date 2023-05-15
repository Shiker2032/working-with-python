

# task 1 Count zeros in input


n = int(input("Input numbers amount"))
cntZero = 0

for i in range(n):
    number = int(input())
    if (number == 0):
        cntZero += 1
print("Amount of zeros", cntZero)


# task 2 count amount of natural dividers

x = int(input("Input number"))
cntNatural = 0

for i in range (1, x + 1):
    if (i == x) or (i == 1) or (x % i == 0):
        cntNatural += 1        
print("Total natural dividers count: ", cntNatural)


# task 3 print all even numbers in range

a = int(input("Input a: "))
b = int(input("Input b: "))
result = ''
while (a <= b):    
    if (a % 2 == 0):
       result = result + " " + str(a)
    a+=1
print(result)
# task 1
print("Input base and height")
b,h = map(int, input().split())
s = (b * h) // 2
print(s)

#task 2
a = 46275

ones = a % 10
tens = (a // 10) % 10
hundreds = (a // 100) % 10
thousands = (a // 1000) % 10
tenThousands = (a // 10000) % 10

result = ((tens ** ones) * hundreds) / (tenThousands - thousands)
print(result)

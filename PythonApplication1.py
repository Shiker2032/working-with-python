# task 1
print("Input a b c sides and height of the triangle")
a, b, c, h = map(int, input().split())
s = (b * h) // 2
p = a + b + c

print("Triangle area:", s)
print ("Triangle perimeter:", p)

#task 2
a = 46275

ones = a % 10
tens = (a // 10) % 10
hundreds = (a // 100) % 10
thousands = (a // 1000) % 10
tenThousands = (a // 10000) % 10

result = ((tens ** ones) * hundreds) / (tenThousands - thousands)
print(result)
# task 1
print("Input a, b sides of the rectangle")
a, b, = map(int, input().split())
s = a * b
p = 2 * (a + b)

print("Rectangle area:", s)
print ("Rectangle perimeter:", p)

#task 2
a = 46275

ones = a % 10
tens = (a // 10) % 10
hundreds = (a // 100) % 10
thousands = (a // 1000) % 10
tenThousands = (a // 10000) % 10

result = ((tens ** ones) * hundreds) / (tenThousands - thousands)
print(result)
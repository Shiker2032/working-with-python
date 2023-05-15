# task 1 check if polyndrome
s1 = input("input polyndrome string ").lower()
polyndrome = s1[::-1].lower()
if (s1 == polyndrome):
    print("yes")
else:
    print("no")


#task 2 remove extra whitespaces
s2 = "  ds   gb frurp  len s   are str   ab ho vi"
s2 = s2.split()
result = ""

if (len(s2) > 1000):
    print("Input shoul be lower that 1000 characters")
else:
    for i in s2:
        result += i + " "
    print(result)
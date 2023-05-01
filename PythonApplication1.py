# task 1
a = int(input("Input number to check "))

if (a < 0):
    if (a % 2 == 0):
        print("Negaitve even number")
    else:
        print("Negative uneven number")
elif(a == 0):
    print("Number is zero")
else:
    if (a % 2 == 0):
        print("Positive even number")
    else:
        print("Positive uneven number")

# task 2
word = str(input("Input word to count vowels and consonants "))
vowels = 0
consonants = 0

for letter in word:
    if (letter == "a") or (letter == "e") or (letter == "i") or (letter == "o") or (letter == "u"):
        vowels += 1
    else:
        consonants += 1
print("Vowels: %i, Consonants: %i" % (vowels, consonants))

#task 3
michael = int(input("Michael cash:"))
ivan = int(input("Ivan cash:"))
min = int(input("Minimum invest amount"))

if (michael >= min) and (ivan >= min):
    print(2)
elif(michael >= min):
    print("Michael")
elif(ivan >= min):
    print("Ivan")
elif (ivan + michael >= min):
    print(1)
else:
    print(0)
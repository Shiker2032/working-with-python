# task 1
def formatAge(age
):
    n = age
    last = int(str(age)[-1])
    suffix = ""

    if (5 <= n <= 20): suffix = "лет"
    elif (last == 1): suffix = "год"
    elif (1 < last < 5): suffix = "года"
    elif (4 < last or last == 0): suffix = "лет"
    return f"{age} {suffix}"

pets = dict()

petName = input("input pet name ")
petKind = input("input pet kind ")
petAge = int(input("input pet age "))
petOwner = input("input owner name ")

pet = dict(
    petKind = petKind,
    petAge = petAge,
    petOwner = petOwner,
)

pets[f"{petName}"] = pet

resultPet = pets[petName]

result = "Это {} по кличке {}. Возраст питомца: {}. Имя владельца: {}".format(resultPet["petKind"], petName, formatAge(resultPet["petAge"]), resultPet["petOwner"])
print(result)

#task 2

i = 10
tmp = dict()
while i > -5:
    tmp[i] = pow(i,i)
    i -= 1

print(tmp)

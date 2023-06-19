# task 1
def formatAge(age
):
    n = age % 10  
    suffix = ("год" if n==1 else 
              "года" if 1<n<5 else 
              "лет")
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


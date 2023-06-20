
## task 1
def factorial (n:int):
    result = 1
    for i in range(n):
        result*=i+1
    return result

def getFactorial (n:int):
    tmp = []
    i = factorial(n)
    while i >= 1:
        tmp.append(factorial(i)) 
        i-=1
    print(tmp)

getFactorial(int(input("input number ")))

## task 2

pets = {

    1:

        {

            "Мухтар": {

                "Вид питомца": "Собака",

                "Возраст питомца": 9,

                "Имя владельца": "Павел"

            },

        },

    2:

        {

            "Каа": {

                "Вид питомца": "желторотый питон",

                "Возраст питомца": 12,

                "Имя владельца": "Саша"

            },

        },

}



def getLastKey ():
     keys = list(pets.keys())
     return keys[-1]

def formatAge(age):
    n = age
    last = int(str(age)[-1])
    suffix = ""

    if (5 <= n <= 20): suffix = "лет"
    elif (last == 1): suffix = "год"
    elif (1 < last < 5): suffix = "года"
    elif (4 < last or last == 0): suffix = "лет"
    return f"{age} {suffix}"


def create ():
     petName = input("input pet name ")
     petKind = input("input pet kind ")
     petAge = int(input("input pet age "))
     petOwner = input("input owner name ")

     pet = {
          petName: {
               "Вид питомца": petKind,
               "Возраст питомца": petAge,
               "Имя владельца": petOwner
          }
     }
     pets[getLastKey() + 1] = pet
     print(pets)

def read():
     id = int(input("input pet id "))
     petData = getPet(id)
     nameKey =  list(petData.keys())
     pet = petData[nameKey[0]]
     result = "Это {} по кличке {}. Возраст питомца: {}. Имя владельца: {}".format(pet["Вид питомца"], nameKey[0], formatAge(pet["Возраст питомца"]), pet["Имя владельца"])
     print(result)


def getPet(id):
    return  pets[id] if id in pets else False    

def update (id):
     petKey = list(pet.keys())[-1]
     newKind = input("input new kind ")     
     newOwner = input("input new owner name ")
     ageInput = input("input new age")  
     newAge = ""

     if (len(ageInput)): newAge = int(ageInput)
     if (len(newKind)):
          pet[petKey]["Вид питомца"] =  newKind
     if(len(str(newAge))):
          pet[petKey]["Возраст питомца"] = newAge
     if(len(newOwner)): pet[petKey]["Имя владельца"] = newOwner
     else: pass
     print(pets)   

def delete(id):
     pets.pop(id)
     print(pets)
 
    
comand = ""
while comand != "stop":
     comand = input("input comand ")

     if comand == "create": create()
     elif comand == "read": 
          petId = int(input("input pet id "))
          pet = getPet(petId)
          if (pet): read(petId)
          else: print("wrong id")
     elif comand == "update":
          petId = int(input("input pet id "))
          pet = getPet(petId)
          if (pet): update(petId)
          else: print("wrong id")
     elif comand == "delete":
          petId = int(input("inpute pet id "))
          pet = getPet(petId)
          if (pet): delete(petId)
          else: print("wrong id")
     else: print("invalid comand")
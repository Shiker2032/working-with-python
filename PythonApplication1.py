# task 1
tmp1 = list(map(int, input("input numbers ").split()))
print("unique numbers: ", len(set(tmp1)))

# task 2
set1 = set(map(int, input("input numbers for first list ").split()))
set2 = set(map(int, input("input numbers for second list ").split()))
print("numbers in both of the lists", len(set1.intersection(set2)))

# task 3
included = set()
tmp3 = list(map(int, input("input numbers to check if they were already included ").split())) 
for el in tmp3:
    if el in included: 
        print("YES")
    else:
        included.add(el)
        print("NO")
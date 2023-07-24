my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def recursiveList (a):
    if (len(a) == 0):
        print("End of the list")
        return
    print(a[0])
    a.pop(0)
    recursiveList(a)
    

recursiveList(my_list)
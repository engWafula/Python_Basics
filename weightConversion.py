weight = int(input("Enter weight: "))
weightType = input("(L)bs or (K)g: ")

if weightType.upper() == "L":
               print(f" You are {weight*0.45} pounds")
elif weightType.upper() == "K" :
                 print(f" You are {weight/0.45} kilos")




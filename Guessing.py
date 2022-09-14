num = 9
i = 1
while i<4:
     n= int(input("Guess: "))
     i = i+1
     if  n==num:
         print("You guessed right")
         break
else:
     print("You have lost")



withdraw=input("How much would you like to withdraw?\n")
ba=11551
hun=withdraw//100
fif=int((withdraw%100))
fifd=(fif//50)
tend=int((withdraw%50))
ten=tend//10
one=int((withdraw%10))
print("Number of 100's is ",hun)
print("Number of 50's is ",fif)
print("Number of 10's is ",ten)
print("Number of 1's is ",one)
balre=int(withdraw-ba)
print("The Amount you have remaining is ",balre)
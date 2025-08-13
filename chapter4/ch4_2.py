print(" *** Digit count and Summation ***")
x = input("Enter an integer : ")
print(f"Entered number = {int(x):,}")
t = len(x)
print(f"Total digits are:  {t}")
i = 0
sum = 0
while i < t :
    number = int(x[i])
    sum += number
    i += 1
print(f"Summation = {sum}")
print("===== End of program =====")
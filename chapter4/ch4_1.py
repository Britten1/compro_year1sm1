print(" *** odd integer summation from 1 to n ***")
x = int(input("Enter an integer(n) : "))
terms = ""
if x <= 0 :
    print(f"The input [{x}] must be greater than or equal to 1 !!!]")
else :
    i = 1
    sum = 0
    while i <= x :
        sum += i
        terms += str(i)
        if i + 2 <= x :
            terms += "+"
        i += 2
    print(f"Summation => {terms} = {sum}")
print("===== End of program ======")

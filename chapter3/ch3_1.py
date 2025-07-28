print(" *** Integer type and odd even ***")
x = int(input("Enter any number : "))
if x < 0 :
    print(f"{x} is negative.")
elif x == 0 :
    print(f"{x} is zero.")
else :
    print(f"{x} is positive.")

if x % 2 == 0 :
    print(f"{x} is even.")
else :
    print(f"{x} is odd.")
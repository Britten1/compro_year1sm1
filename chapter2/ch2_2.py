print(" *** Number Fun ***")
x = int(input("Enter a 3-digit number : "))
square = x ** 2
decimal = x * 0.25
flipping = str(x)
y = ((x % 10) * 10) + (((x // 10) % 10) * 10) + (x // 100)
hexa = hex(x)[2:]
print("")
print("You have entered     =>",x)
print(f"Square               => {square:,}")
print(f"25% 3 decimal places => {decimal:,.3f}%")
print("Flipping             =>",y)
print(f"Hexadecimal          => {hexa} or {hexa.upper()}")
print(f"Binary               => {x:b}")
print(f"Binary right 8-digit => {x//16%16:04b} {x%16:04b}")
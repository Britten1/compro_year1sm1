print(" *** Pyramid-V ***")
x = int(input("Enter height : "))
row = 0

while row < x-1 :
    col = 0 
    while col < 2*x - 1:
        if row + col < x -1 :
            print(" ", end='')
        col += 1
    print("/",end='')
    print("."*(row * 2 ), end='')
    print("\\")
    row += 1

print("/", end='')
print("_" * ((x - 1) * 2 ), end='')
print("\\")

print("===== End of program =====")
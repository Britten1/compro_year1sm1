print(" *** Linear Formula ***")
x1, y1, x2, y2 = input("Enter x1 y1 x2 y2: ").split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)


print(f"({x1},{y1}) ==> ({x2},{y2})")

if x1 == x2:
    print(f"Vertical line ==> x = {x1}.")
    print(f"===== End of program =====")
else:
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    print(f"f1 ==> {A}x + {B}y + {C} = 0")

    a = A
    b = B
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b != 0:
        temp = b
        b = a % b
        a = temp
    g = a

    c = C
    if c < 0:
        c = -c
    while c != 0:
        temp = c
        c = g % c
        g = temp

    if g != 0:
        A = A // g
        B = B // g
        C = C // g

    print(f"f2 ==> {A}x + {B}y + {C} = 0")

    if A < 0 or (A == 0 and B < 0):
        A = -A
        B = -B
        C = -C

    f3 = "f3 ==> "

    if A == 1:
        f3 += "x"
    elif A == -1:
        f3 += "-x"
    else:
        f3 += f"{A}x"

    if B > 0:
        if B == 1:
            f3 += " + y"
        else:
            f3 += f" + {B}y"
    elif B < 0:
        if B == -1:
            f3 += " - y"
        else:
            f3 += f" - {-B}y"

    if C > 0:
        f3 += f" + {C}"
    elif C < 0:
        f3 += f" - {-C}"

    f3 += " = 0"

    print(f"{f3}")
    print(f"===== End of program =====")
print(" *** Fibonacci sequence ***")
x = input("Enter a0 a1 n : ")
a1,a0,n = x.split()
a0 = int(a0)
a1 = int(a1)
n = int(n)
count = 0
while count < n :
    if count == 0 :
        print(a0 , end="")
        p = a0
    elif count == 1 :
        print(", " + str(a1), end="")
        c = a1
    else :
        nt = p + c
        print(", " + str(nt), end="")
        p,c=c,nt
    count += 1
print("\n===== End of program =====")
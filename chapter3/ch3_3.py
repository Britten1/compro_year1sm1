print(" *** Data type integer float string ***")
cei = input("Enter a word : ")

try :
    num = float(cei)
    if num.is_integer() :
        print(f"{int(num)} * 2 = {int(num) * 2}")
    else :
        print(f"{num:.3f} / 3 = {num / 3:.3f}")
except ValueError :
    print(f"{cei} {cei} {cei}")
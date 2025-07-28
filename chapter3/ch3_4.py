print(" *** Water Supply Calculator ***")
unit = int(input("Total usage : "))
bill = 0
if unit <= 10 :
    bill = unit * 5
elif unit <= 50 :
    bill = (10*5) + ((unit-10) * 10)
elif unit <= 100 :
    bill = (10*5) + (40*10) + ((unit-50) * 12)
elif unit <= 500 :
    bill = (10*5) + (40*10) + (50*12) + ((unit-100) * 15)
elif unit <= 1000 :
    bill = (10*5) + (40*10) + (50*12) + (400*15) + ((unit-500) * 18)
elif unit <= 5000 :
    bill = (10*5) + (40*10) + (50*12) + (400*15) + (500*18) + ((unit-1000) * 20)
elif unit > 5000 :
    bill = (10*5) + (40*10) + (50*12) + (400*15) + (500*18) + (4000*20) + ((unit-5000) * 21)
print(f"Total Amount = {bill:,.2f} baht")
print("===== End of program =====")
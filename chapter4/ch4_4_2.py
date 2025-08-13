print(" *** Prime number summation ***")
data = input("Enter start stop max_sum : ")
start, stop, max_sum = data.split()
start = int(start)
stop = int(stop)
max_sum = int(max_sum)

if start >= stop:
    print("Invalid input !!!")
    print("===== End of program =====")
else:
    num = start
    total = 0
    count = 0
    result = ""

    while num <= stop:
        if num > 1:
            d = 2
            is_prime = 1
            while d * d <= num:
                if num % d == 0:
                    is_prime = 0
                d += 1

            if is_prime == 1 and total + num <= max_sum:
                if result != "":
                    result += "+"
                result += str(num)
                total += num
                count += 1

        if total >= max_sum or num == stop:
            num = stop + 1
        else:
            num += 1

    print(f"{result} = {total:,}")
    print(f"Total = {count}")
    print("===== End of program =====")
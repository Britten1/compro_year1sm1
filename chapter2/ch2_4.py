print(" *** Distance *** ")
u,a,t = input("Enter Velocity Acceleration Time: ").split(',')
x = float(u)
y = float(a)
z = float(t)
s1 = x * z
s2 = (y* (z ** 2)) / 2
s3 = s1 + s2
print(f"Your Distance = {s3:,.2f}")
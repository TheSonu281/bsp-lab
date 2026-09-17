f1 = 0
f2 = 1
n = int(input("Enter range: "))
print("fibonacci series:")
for i in range(n):
    print(f1, end="")
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    
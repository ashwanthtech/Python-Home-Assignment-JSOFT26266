a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your thrid number: "))

if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print ("Largest =", c)
    

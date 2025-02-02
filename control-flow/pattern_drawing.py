size = int(input("Enter the size of the pattern: "))
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")  
    print()  
    row += 

print("ASSIGNMENT 4 - HW1 - BY CAO PHONG")
def is_prime(n):
    if n < 2:
        return False
    for b in range(2, n):
        if n % b == 0:
            return False
    return True
while True:
        try:
            numbers = int(input("Huh,What is your number ?: "))
            break
        except ValueError:
            print("You...you sure that an integer? OH HELL NAH, Try again mate.")
        
if is_prime(numbers):
    print("Your number is a prime number.")
else:
    print("Your number is NOT a prime number.")



biggest = None
smallest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    num = float(user_input)
    if biggest is None or num > biggest:
        biggest = num
    if smallest is None or num < smallest:
        smallest = num
print("The biggest number is:", biggest)
print("The smallest number is:", smallest)
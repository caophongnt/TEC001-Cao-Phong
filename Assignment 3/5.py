user_input = input("Enter Your Word: ")
print("- " * 10)
if len(user_input) % 2 != 0:
    user_input = user_input[len(user_input)//2]
    print(user_input)
else:
    print(user_input[len(user_input)//2 - 1:len(user_input)//2 + 1])              
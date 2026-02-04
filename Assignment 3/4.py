def login_system():
    attempts = 0
    max_attempts = 5
    print(" Welcome to Login System >ᴗ< ")
    while attempts < max_attempts:
        attempts += 1
        username = input("Enter username: ")
        print("\n")
        print("----------------- ´꒳` -----------------" )
        password = input("Enter password: ")
        print("\n")
        print("----------------- ´꒳` -----------------" )
        if username == "python" and password == "rules":
            print("\n")
            print("Welcome")
            return
        elif username != "python" or password != "rules":
            print("\n")
            print("Try again")
        if attempts == max_attempts:
            print("\n")
            print("Access denied (¬_¬)💢 ")

        
login_system()
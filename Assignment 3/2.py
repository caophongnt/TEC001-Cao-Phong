while True: 
    inches = float(input("Enter value in inches: "))
    if inches < 0:
        break
    centimeter = inches * 2.54 
    print(centimeter)
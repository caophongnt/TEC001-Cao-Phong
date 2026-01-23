def hemoglobin_check():
    sex = input("Enter your biological sex (F for female, M for male): ").upper()
    if sex not in ['F', 'M']:
        print("Invalid sex entered.")
        return
    value = float(input("Enter your hemoglobin value (g/l): "))
    if sex == 'F':
        if value < 117:
            print("Your hemoglobin value is low.")
        elif value <= 155:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")
    else:  
        if value < 134:
            print("Your hemoglobin value is low.")
        elif value <= 167:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is high.")
hemoglobin_check()
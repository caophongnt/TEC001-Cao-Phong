def check_zander():
    length = float(input("Enter the length of the zander in centimeters: "))
    if length < 42:
        below = 42 - length
        print("Release the fish back into the lake. It is " + str(below) + " centimeters below the size limit.")
    else:
        print("The zander meets the size limit.")
check_zander()
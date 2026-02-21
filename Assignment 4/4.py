print("ASSIGNMENT 4 - HW4 - BY CAO PHONG")
def sum_list(numbers):
    total = 0
    for num in numbers:   
        total = total + num
    return total
def main():
    my_numbers = [5, 10, 15, 20, 25]
    result = sum_list(my_numbers)
    print("The sum of the list is:", result)
if __name__ == "__main__":
    main()

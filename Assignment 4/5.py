print("ASSIGNMENT 4 - HW5 - BY CAO PHONG")
def remove_odds(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main(): 
    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = remove_odds(my_numbers)
    print("Original list:", my_numbers)
    print("List without odd numbers:", result)
if __name__ == "__main__":
    main()
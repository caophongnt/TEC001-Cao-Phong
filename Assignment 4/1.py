def main():
   numbers = []
   print("ASSIGNMENT 4 - HW 1 - BY CAO PHONG")
   while True:
      user_input = input("INPUT NUMBERS: ")
      if user_input == "":
         break
      try:
        number = float(user_input)
        numbers.append(number)
      except ValueError:
        print("Nah that's not a number, try again pal.")
   numbers.sort(reverse=True)
   top_5 = numbers[:5]
   print("Top 5 numbers: ", top_5)
if __name__ == "__main__":
      main()

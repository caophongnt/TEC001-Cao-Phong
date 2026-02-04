phrase = input("Enter a phrase: ").split()
acronym = []
for word in phrase:
    acronym.append(word[0].upper())
    a = ''.join(acronym)
print("The acronym is:", a)
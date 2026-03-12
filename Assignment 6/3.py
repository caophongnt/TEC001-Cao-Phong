def main():
    names = set()
    while True:
        name = input("nhập tên : ")
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    print("\nDanh sách tên đã nhập: ")
    for name in names:
        print(name)
if __name__ == "__main__":
    main()
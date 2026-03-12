def main():
    seasons = ("winter", "spring", "summer", "autumn")

    month = input("Bạn muốn biết mùa của tháng nào | 0_0 | ? ")
    if not month.isdigit():
        print("Nhập số nguyên nha trời | x_x |")
        return

    month = int(month)
    if month < 1 or month > 12:
        print("1 năm có 12 tháng thôi mà trời { 0w0 }.")
        return

    if month == 12 or month == 1 or month == 2:
        season = seasons[0]
    elif month >= 3 and month <= 5:
        season = seasons[1]
    elif month >= 6 and month <= 8:
        season = seasons[2]
    else:  
        season = seasons[3]

    print(f"Tháng {month} là mùa {season}.")

if __name__ == "__main__":
    main()
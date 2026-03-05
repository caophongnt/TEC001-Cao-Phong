import random
N = int(input("Nhập số điểm ngẫu nhiên: "))
n = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1 
pi_approximation = 4 * n / N
print('---------KABOOM---------')
print(f"Số điểm trong hình tròn: {n}")
print(f"Tổng số điểm: {N}")
print(f"Giá trị π xấp xỉ: {pi_approximation}")
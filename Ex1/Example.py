n = int(input("Nhap n = "))
s = 0
#  3 - Tính S(n) = 1 + 1/2 + 1/3 + … + 1/n

# for i in range(1, n + 1):
#     s += 1/i
# 4 - Tính S(n) = 1/2 + 1/4 + … + 1/2n
for i in range(1, n + 1):
    s += 1/(2*i)
#5 - Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n - 1)
for i in range(1, n + 1):
    s += 1/(2*i -1)
print("S = " ,s)
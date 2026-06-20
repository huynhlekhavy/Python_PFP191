menu = [
    "Tam giác vuông góc trái dưới",
    "Tam giác vuông góc phải dưới",
    "Tam giác vuông góc trái trên",
    "Tam giác vuông góc phải trên",
    "Tam giác vuông góc trái dưới (rỗng)",
    "Tam giác vuông góc phải dưới (rỗng)",
    "Tam giác vuông góc trái trên (rỗng)",
    "Tam giác vuông góc phải trên (rỗng)",
    "Tam giác đều",
    "Hình chữ nhật đầy",
    "Hình chữ nhật rỗng",
    "Hình vuông đầy",
    "Hình vuông rỗng",
    "Hình thoi",
    "Hình bình hành",
    "Hình bình hành rỗng",
    "Hình chữ nhật",
    "Tam giác chữ rỗng",
    "Hình thoi rỗng",
    "Hình chữ X",
    "Tam giác vuông góc phải số",
    "Tam giác vuông góc trái số",
    "Hình bình hành rỗng số",
    "Hình chữ nhật số đầy",
    "Hình vuông số",
    "Hình vuông số rỗng",
    "Hình thoi số",
    "Hình tam giác chữ rỗng",
    "Hình thoi chữ",
    "Kim tự tháp số/chữ đối xứng",
    "Tam giác vuông rỗng số",
    "Tam giác vuông số",
    "Tam giác vuông số rỗng",
    "Hình bình hành rỗng chữ",
    "Tam giác vuông rỗng chữ",
    "Tam giác đều chữ",
    "Hình thoi chữ rỗng"
]

print("# ============================")
print("# Điều hướng")
print("# ============================")

for i, ten_bai in enumerate(menu, start=1):
    print(f"Bài tập {i}: {ten_bai}")

#18 -> A->Z 65-> 89 a->z 97->121
def bai18(n):
    for i in range(1, n+1):
        if i ==1:
            print("A", end="")
        elif i == n:
            for j in range(i):
                print(chr(65 + j), end=" ")
        else:
            print("A", end="")
            print(" " * (2*i-3), end="")
            print(chr(64 + i), end=" ")
        print()
bai18(10)
#30
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
def bai30(n):
    for i in range(1, n+1):
        print("  " * (n - i), end="")
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end=" ")
        print()
bai30(5)
#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A
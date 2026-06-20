import math
# ============================
# Điều hướng
# ============================
print("Bài tập 1: Xếp loại học sinh theo điểm số")
print("Bài tập 2: Xác định loại hình tam giác")
print("Bài tập 3: Giải phương trình bậc hai")
print("Bài tập 4: Kiểm tra năm nhuận")
print("Bài tập 5: Phân loại người dùng theo độ tuổi")
print("Bài tập 6: Kiểm tra tháng có 31 ngày")
print("Bài tập 7: Tính số ngày trong tháng")
print("Bài tập 8: Xác định mùa trong năm")
print("Bài tập 9: Kiểm tra ngày trong tháng 2")
print("Bài tập 10: Xác định kỳ học FPT")
print("\n======================================\n")

#Bai 2 -> hieu dc dung dau **
def loai_tam_giac(a,b,c):
    if a == b == c:
        return "Tam giac deu"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "Tam giac vuong"
    elif a!=b and b!=c and a!=c:
        return "Tam giac nhon"
    else:
        return "Tam giac tu"

a = int(input(""))
b = int(input(""))
c = int(input(""))
print(f"{loai_tam_giac(a,b,c)}")
# Bai 3 sqrt() can bac 2 -> cbrt() can bac 3 -> delta ** (1/2)
def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0 :
        x1 = (-b + math.sqrt(delta)) / (2*a)
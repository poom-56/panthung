# 1. ฟังก์ชันบวกเลข 2 ตัว
def add_numbers(a, b):
    return a + b

# ตัวอย่างใช้งาน
print("1. ผลบวก:", add_numbers(5, 3))


# 2. ฟังก์ชันยกกำลังสองเลข 1 ตัว
def square_number(a):
    return a ** 2

# ตัวอย่างใช้งาน
print("2. กำลังสอง:", square_number(4))


# 3. ฟังก์ชันแปลงเลขเดือนเป็นชื่อเดือน
def month_name(month_number):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return "เลขเดือนไม่ถูกต้อง"

# ตัวอย่างใช้งาน
print("3. เดือนที่เลือก:", month_name(5))


# 4. ฟังก์ชันต่อสายอักขระ 3 ตัว
def concatenate_strings(str1, str2, str3):
    return str1 + str2 + str3

# ตัวอย่างใช้งาน
print("4. ผลต่อสายอักขระ:", concatenate_strings("Hello, ", "World", "!"))  



# 5. ฟังก์ชันลดราคาสินค้า
def apply_discount(price, discount):
    return price * (1 - discount/100)

# ตัวอย่างใช้งาน
print("5. ราคาหลังลด:", apply_discount(1000, 20))

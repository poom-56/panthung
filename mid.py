
def calculate_parking_fee(hour, minute):
    try:
        hour = int(hour)
        minute = int(minute)
    except ValueError:
        return "โปรดใส่ข้อมูลที่เป็นตัวเลข"

    total_minutes = hour * 60 + minute

    if total_minutes <= 60:
        return 0
    else:
        extra_minutes = total_minutes - 60
        # ปัดเศษขึ้นเป็นชั่วโมง
        extra_hours = (extra_minutes + 59) // 60
        return extra_hours * 30


# ตัวอย่างการใช้งาน
h = input("กรุณาใส่ชั่วโมง: ")
m = input("กรุณาใส่นาที: ")
result = calculate_parking_fee(h, m)
print("ค่าจอดรถ:", result)
*--------------------------------------------------------------------------------*
def calculate_operations():
    try:
        m = int(input("กรอกตัวเลขตัวที่ 1: "))
        n = int(input("กรอกตัวเลขตัวที่ 2: "))

        print("ผลบวก =", m + n)
        print("ผลลบ =", m - n)
        print("ผลคูณ =", m * n)

        if n != 0:
            print("ผลหาร =", m / n)
        else:
            print("ไม่สามารถหารด้วยศูนย์ได้")

    except ValueError:
        print("โปรดใส่ข้อมูลที่เป็นตัวเลขจำนวนเต็มเท่านั้น")

# เรียกใช้งานฟังก์ชัน
calculate_operations()
*--------------------------------------------------------------------------------*
# รับค่า a และ b จากผู้ใช้
a = int(input("กรอกค่า a: "))
b = int(input("กรอกค่า b: "))

# สลับค่า
a, b = b, a

# แสดงผลลัพธ์หลังสลับ
print("a =", a)
print("b =", b)
*--------------------------------------------------------------------------------*
i = 0
while i <= 100:
    print(i)
    i += 1
*--------------------------------------------------------------------------------*
i = 1000
while i >= 0:
    print(i)
    i -= 1
*--------------------------------------------------------------------------------*
min_value = None

while True:
    user_input = input("กรอกจำนวนจริง (หรือหยุดด้วยค่าที่ไม่ใช่จำนวน): ")
    try:
        num = float(user_input)
        if min_value is None or num < min_value:
            min_value = num
    except ValueError:
        break

if min_value is not None:
    print("ค่าที่น้อยที่สุดคือ:", min_value)
else:
    print("ไม่มีจำนวนจริงที่รับเข้ามาเลย")
*--------------------------------------------------------------------------------*
scores = []
i = 0

while i < 5:
    try:
        score = float(input(f"กรอกคะแนนตัวที่ {i+1}: "))
        scores.append(score)
        i += 1
    except ValueError:
        print("โปรดกรอกตัวเลขเท่านั้น")

average = sum(scores) / len(scores)
print("ค่าเฉลี่ยของคะแนนทั้งหมดคือ:", average)

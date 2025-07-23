#------------------BMI-------------------------
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    result = "BMI is {:.1f}".format(bmi)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return result, category

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

result, category = calculate_bmi(weight, height)
print(result)
print(category)
#---------------------Card----------------------
income = float(input("กรุณากรอกรายได้ต่อเดือน (บาท): "))

if income < 15000:
    print("ขออภัย คุณยังไม่สามารถสมัครบัตรเครดิตได้ (ต้องมีรายได้อย่างน้อย 15,000 บาท)")
elif income < 30000:
    print("ขออภัย รายได้ของคุณยังไม่ผ่านเกณฑ์การอนุมัติวงเงินบัตรเครดิต")
elif 40000 <= income <= 69999:
    print("คุณสามารถสมัครบัตรเครดิตประเภท 'บัตรเงิน' ได้")
elif 70000 <= income <= 99999:
    print("คุณสามารถสมัครบัตรเครดิตประเภท 'บัตรทอง' ได้")
elif income > 100000:
    print("คุณสามารถสมัครบัตรเครดิตประเภท 'บัตร Platinum' ได้")
else:
    print("คุณสามารถสมัครบัตรเครดิตได้ แต่ไม่เข้าข่ายบัตรเงิน/ทอง/Platinum")

#---------------------Password----------------------
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "Ad13n@23t":
    print("Welcome, admin")
else:
    print("You are not admin")
#---------------------Polo----------------------
chest_size = float(input("กรุณากรอกขนาดหน้าอก (นิ้ว): "))

if chest_size <= 34:
    size = "XS"
elif chest_size <= 36:
    size = "S"
elif chest_size <= 38:
    size = "M"
elif chest_size <= 40:
    size = "L"
else:
    size = "XL"
print(f"ขนาดเสื้อที่เหมาะสมคือ: {size}")
#---------------------Score----------------------
score = int(input("กรุณากรอกคะแนน (จำนวนเต็ม): "))

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"คะแนนของคุณคือ {score} ได้เกรด: {grade}")
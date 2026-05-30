
patient_name = input("Nhap ho ten benh nhan : ")

patient_id = input("Nhap ma benh nhan : ")

department_name = input("Nhap khoa kham : ")

body_temperature_input = input("Nhap nhiet do co the: ")

heart_rate_input = input("Nhap nhip tim : ")

body_weight_input = input("Nhap can nang: ")


body_temperature = float(body_temperature_input)

heart_rate = int(heart_rate_input)

body_weight = float(body_weight_input)


print("Ho ten benh nhan :", patient_name)
print("Ma benh nhan :", patient_id)
print("Khoa kham  :", department_name)
print("Nhiet do  :", body_temperature, "do C")
print("Nhip tim  :", heart_rate, "nhip/phut")
print("Can nang :", body_weight, "kg")

print("Dang ky kham thanh cong!")

print("patient_name : ",type(patient_name))
print("patient_id :", type(patient_id).__name__)
print("department_name :", type(department_name))
print("body_temperature :", type(body_temperature))
print("heart_rate   :", type(heart_rate))
print("body_weight  :", type(body_weight))


# luồng chương trình
# Bắt đầu chương trình

# Thu thập:
# - Họ tên
# - Mã bệnh nhân
# - Khoa khám
# - Nhiệt độ
# - Nhịp tim
# - Cân nặng

# Ép kiểu dữ liệu:
# - float cho nhiệt độ
# - int cho nhịp tim
# - float cho cân nặng


# Hiển thị Log hệ thống bằng type()

# Kết thúc chương trình

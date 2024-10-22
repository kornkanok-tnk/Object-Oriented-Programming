print('โปรแกรมคำนวณเกรด')
a = int(input('โปรดใส่คะแนน : '))
if a < 0 or a > 100 :
    print('กรอกคะแนน')
elif a >= 80 :
    print('เกรด4')
elif a >= 70 :
    print('เกรด3')
elif a >= 60 :
    print('เกรด2')
elif a >= 50 :
    print('เกรด1')
else :
    print('สอบตกจ้า')
    print('ต้องการสอบแก้ ถ้าต้องการกด1 ไม่ต้องการกด2 ')
    b = int(input('กรอกตัวเลือก : '))
    if b == 1:
        score1 = 50 - a
        print(f'คุณขาดคะแนนอีก {score1}')
    elif b == 2 :
        print('สอบตกเหมือนดิม')
    else:
        print('กรุณาเลือก 1 และ 2')
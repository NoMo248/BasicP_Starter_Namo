member = (input("ลูกค้ามีสมาชิกไหมครับ ระด้บไหนครับ gold,silver none "))
price = int(input("ราคารวม ")) 
gold1 = price * 15/100 
gold2 = price * 10/100 
silver1 = price * 10/100
silver2 = price * 5/100
day5per = price * 5/100
none = price 
if member == "gold":
    if price >= 1000:
        print("ได้รับส่วนลด 15 เปอร์เซ็น")
        print(gold1 , "บาท")
        print(price - gold1, "บาท")
    else:
        print("ได้รับส่วนลด 10 เปอร์เซ็น")
        print(gold2 , "บาท")
        print(price - gold2, "บาท")
elif member == "silver":
    if price >= 1000:
        print("ได้รับส่วนลด 10 เปอร์เซ็น")
        print(silver1 , "บาท")
        print(price - silver1, "บาท")
    else:
        print("ได้รับส่วนลด 5 เปอร์เซ็น")
        print(silver2 , "บาท")
        print(price - silver2, "บาท")
elif member == none:
    print(price , "บาท")
price2 = price - gold1
price3 = price - gold2
price4 = price - silver1
price5 = price - silver2
day = int(input("วันที่สั่งซื้อ "))
even = day %2 == 0
if day == even:
    print(price)
else:
    if price > 800:
        print("ได้รับส่วนลดเพิ่มอีก 5 เปอร์เซ็น")
        print(day5per, "บาท")
        print("ราคารวม")
    elif price < 800:
        print("คิดค่าส่ง 50 นะจ๊ะ")
        print(price + 50,"บาท")
    else:
        print("ส่งฟรี")
        print(price - day5per)
        
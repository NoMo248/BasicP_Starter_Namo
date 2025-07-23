member = (input("ลูกค้ามีสมาชิกไหมครับ ระด้บไหนครับ gold,silver none "))
price = int(input("ราคารวม ")) 
day = int(input("วันที่สั่งซื้อ "))
gold1 = price * 15/100 
gold2 = price * 10/100 
silver1 = price * 10/100
silver2 = price * 5/100
none = price 
if member == "gold":
    if price >= 1000:
        print("ได้รับส่วนลด 15 เปอร์เซ็น")
        print(gold1 , "บาท")
        print(price - gold1)
    else:
        print("ได้รับส่วนลด 10 เปอร์เซ็น")
        print(gold2 , "บาท")
        print(price - gold2)
elif member == "silver":
    if price >= 1000:
        print("ได้รับส่วนลด 10 เปอร์เซ็น")
        print(silver1 , "บาท")
        print(price - silver1)
    else:
        print("ได้รับส่วนลด 5 เปอร์เซ็น")
        print(silver2 , "บาท")
        print(price - silver2)
elif member == none:
    print(price , "บาท")
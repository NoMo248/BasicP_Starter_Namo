
x = int(input( "ระยะทางกี่กิโลครับโผม = "))
y = 0 
num1 = y*7/100
if x < 5:
    print(x) , print("km")
    print("ส่งฟรีนะจ๊ะ")
elif 5 <= x <= 50:
    y = 10
    print(x,"km")
    print("10 baht")
    print("ภาษี",y*7/100)
    print("รวมเป็น",y*107/100,"baht")
elif 51 <= x <= 100:
    y = 15
    print(x,"km")
    print("15 baht")
    print("ภาษี",y*7/100)
    print("รวมเป็น",y*107/100,"baht")
elif 101 <= x <= 300:
    y = 25
    print(x,"km")
    print("25 baht")
    print("ภาษี",y*7/100)
    print("รวมเป็น",y*107/100,"baht")
elif 301 <= x <= 500:
    y = 35
    print(x,"km")
    print("35 baht")
    print("ภาษี",y*7/100)
    print("รวมเป็น",y*107/100,"baht")
else : 
    y = 45
    print(x,"km")
    print("45 baht")
    print("ภาษี",y*7/100)
    print("รวมเป็น",y*107/100,"baht")
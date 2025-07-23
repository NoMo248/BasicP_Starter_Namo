monster = 43172
stareintoitsoul = 1
sword = 21.5
AmericanStyle = 86
holyminecraftstick = 21586
print("สู้ป่าวๆๆๆๆๆ กลัวรึป่าวๆๆๆ กด 1 สู้ 2 หนี ")
x = int(input("1 or 2 ตอบ "))
if x == 1:
    print("ดีมากที่เลือกสู้ เริ่มก่อนเลยจากการเลือกอาวุธก่อน มี 1.stareintoitsoul (emotional damage) 2.sword 3.AmericanStyle 4.holyminecraftstick แต่ละอาวุธดาเมจไม่เท่ากันเลือก ")
elif x == 2:
    print("nuh uh หนีไม่รอด GGez สู้อยู่ดีบังคับ เริ่มก่อนเลยจากการเลือกอาวุธก่อน มี 1.stareintoitsoul (emotional damage) 2.sword 3.AmericanStyle 4.holyminecraftstick แต่ละอาวุธดาเมจไม่เท่ากันเลือก ")
else:
    print("หนีไปไหนไม่รอดหรอก กลับไปเลือกอาวุธ มี 1.stareintoitsoul (emotional damage) 2.sword 3.AmericanStyle 4.holyminecraftstick แต่ละอาวุธดาเมจไม่เท่ากันเลือก")

weapon = int(input("อาวุธเลข??? "))
print(weapon , "ok")
print("จะตีกี่รอบ??? คิดดีดีนะ เพราะถ้าไม่ตีให้มันตายพอดี มันจะเกิดใหม่")
num = int(input("ตีกี่รอบจ๊ะ "))
weapon1 = 1
weapon2 = 21.5
weapon3 = 86
weapon4 = 21586

i = 1
while i <= num:
    if weapon == 1:
        monster = monster - weapon1
        print(f"ครั้งที่ {i} hp left", monster)
    elif weapon == 2:
        monster = monster - weapon2
        print(f"ครั้งที่ {i} hp left", monster)
    elif weapon == 3:
        monster = monster - weapon3
        print(f"ครั้งที่ {i} hp left", monster)
    elif weapon == 4:
        monster = monster - weapon4
        print(f"ครั้งที่ {i} hp left", monster)
    else:
        print("you want to use your own hand??? go back and choose again")
    i=i+1
    if monster == 0:
            print("BOSS DEFEATED")
    elif monster < 0:
            print("พี่ก็ตีแรงเกิน บอสเลือดติดลบสกิลทำงาน")
            print("BOSS had respawn")
            monster = 86
            weapon = int(input("เอาใหม่ๆรอบนี้เลือกอาวุธเลข??? "))
            print("จะตีกี่รอบ??? คิดดีดีนะรอบนี้")
            num = int(input("ตีกี่รอบจ๊ะ "))
            if weapon == 1:
                monster = monster - weapon1
                print(f"ครั้งที่ {i} hp left", monster)
            elif weapon == 2:
                monster = monster - weapon2
                print(f"ครั้งที่ {i} hp left", monster)
            elif weapon == 3:
                monster = monster - weapon3
                print(f"ครั้งที่ {i} hp left", monster)
            elif weapon == 4:
                monster = monster - weapon4
                print(f"ครั้งที่ {i} hp left", monster)
            if monster == 0:
                print("BOSS DEFEATED")
            else:
                print("YOU DEAD WHY SO NOOB")
            
            

    

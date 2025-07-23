monster = 43172
sword = monster - 21.5
AmericanStyle = monster - 86
holyminecraftstick = 21586
print("สู้ป่าวๆๆๆๆๆ กลัวรึป่าวๆๆๆ กด 1 สู้ 2 หนี ")
x = int(input("1 or 2 ตอบ "))
if x == 1:
    print("ดีมากที่เลือกสู้ เริ่มก่อนเลยจากการเลือกอาวุธก่อน มี 1.sword 2.AmericanStyle 3.holyminecraftstick แต่ละอาวุธดาเมจไม่เท่ากันเลือก ")
else:
    print("nuh uh หนีไม่รอด GGez สู้อยู่ดีบังคับ เริ่มก่อนเลยจากการเลือกอาวุธก่อน มี 1.sword 2.AmericanStyle 3.holyminecraftstick แต่ละอาวุธดาเมจไม่เท่ากันเลือก ")
weapon = int(input("อาวุธเลข??? "))
print(weapon)
print("จะตีกี่รอบ??? คิดดีดีนะ เพราะถ้าไม่ตีให้มันตายพอดี มันจะเกิดใหม่")
num = int(input("ตีกี่รอบจ๊ะ "))
weapon1 = 21.5
weapon2 = 86
weapon3 = 21586

i = 1
while i <= num:
    monster = monster - weapon1
    print(f"ครั้งที่ {i} hp left", monster)
    i=i+1

    

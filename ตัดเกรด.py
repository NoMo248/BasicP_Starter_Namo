x = int(input(" ได้คะแนนเท่าไหร่??? "))
if x >= 50 and x <= 100:
    print("ดีมากที่ผ่านมาได้")
    if x >= 80:
        print("Grade A" , ("สุดยอดมาก 😎"))
    elif x >= 70:
        print("Grade B" , ("ถือว่าเยี่ยม 😁"))
    elif x >= 60:
        print("Grade C" , ("เกือบหลับแต่ยังไหว 🫠"))
    elif x >=50:
        print("Grade D" , ("พี่จ๋าไม่ไหวแล้ว 😭"))
elif x < 50 and x >= 0:
        print("Grade F" , ("ต่อให้เทอมนึง ค่อยเอาจริง💀"))
else:
    print("เดี๋ยวๆๆๆ ทำไปด้ายยางงายว่ะเห้ย")
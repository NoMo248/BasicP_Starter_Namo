def Grade(score):
    if score >= 50:
        print("you passed")
        if score >= 80:
            print("Grade : A")
        elif score >= 70:
            print("Grade : B")
        elif score >= 60:
            print("Grade : C")
        elif score >= 50:
            print("Grade : D")
    else:
        print("you failed")

Grade(82)
Grade(64)
Grade(86)
Grade(80)
Grade(79)
Grade(54)
Grade(70)
Grade(3.1428)
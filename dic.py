student = {
    "name" : "Namo" ,
    "id" : "68130500033",
    "year" : "1"
}
print(f"My name is {student['name']}")
student['name'] = "Oman"
print(f"My name is {student['name']}")
print("------------------")
print(student)
student['grade'] = "S+++"
print(student)
student.pop("grade")
print(student)

print("------------------")

student = {
    "name" : "Namo" , "id" : "68130500033" , "age" : "20" 
}
print(student)
for s in student:
    print(student)    
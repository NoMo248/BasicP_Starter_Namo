student = [
    {"name": "Namo" , "id" : "68130500033" , "age" : 18},
    {"name": "Namo" , "id" : "68130500033" , "age" : 1000},
    {"name": "Namo" , "id" : "68130500033" , "age" : 2000},
]
def data(ds, index , key) :
    return ds[index][key]
print(data(student, 2 , "age"))
print (student)

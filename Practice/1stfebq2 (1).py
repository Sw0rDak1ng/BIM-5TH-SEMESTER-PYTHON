def myfunction(student):
    student1=[]
    for x in student:
        if x.lower().startswith('s'):
            student1.append(x)
    return student1
students=[]
for i in range(6):
    n=input("Enter the name of student: ")
    students.append(n)
print(myfunction(students))


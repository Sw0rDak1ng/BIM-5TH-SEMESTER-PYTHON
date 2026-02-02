# write a program to input name of 5 students in a list,pass the list to a user defined function that returns the list of students that start with 'S'

def myfunction(student):
    student1 = []
    for x in student:
        if x.lower().startswith('s'):
            student1.append(x)
    return student1

student=[]
for i in range(5):
    name=input("Enter the name of the student:")
    student.append(name)

result=myfunction(student)
print('Students starting with 'S'',result)


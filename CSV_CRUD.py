# import csv
# import pprint
# f=open("C:\\Users\\LENOVO\\OneDrive\\Documents\\students_data(1).csv")

# data=csv.reader(f)

# list1.append(rec)
    
    
    # pprint.pprint(list1)


    # greater thean 90
# for rec in list1:
#     if  int(rec[2])>90:
#         print(rec)   

# greater than 40
# for rec in list1:
#     if int(rec[2])>40:
# f.close()

# f2=open("C:\\Users\\LENOVO\\OneDrive\\Documents\\faculties_data(1) gen ai.csv")
# data=csv.reader(f2)
# list2=[]
# for rec in data:
#     list2.append(rec)
#     pprint.pprint(list2)

# for rec in list2:
#     if rec[1]
        
#       print(rec)


# pprint.pprint(list1)
# list2=[]
# for rec in list1:
#         if rec[1].lower()=="physics":
#               print([rec[0],rec[2]])
            # list2.append([rec[0],rec[2]]) 
             # print(list2)
             
import csv
f=open("C:\\Users\\LENOVO\\OneDrive\\Documents\\students_data(1).csv")
data=csv.reader(f)
student_marks={}
for rec in data:
    student=rec[0]
    marks=rec[2]
    if int(marks) < 35:
        ...
    else:
        if student not in student_marks:
            student_marks[student] = [int(marks)]
        else:
            student_marks[student].append(int(marks))  
_min = min(student_marks.items(), key=lambda x: sum(x[1]))
print(_min)
# print(student_marks)
for j in student_marks:
    if sum(student_marks[j]) == sum(_min[1]):
        print(j)      
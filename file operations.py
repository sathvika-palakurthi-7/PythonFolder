import csv
student={}
f=open(":\\Users\\LENOVO\\OneDrive\\Documents\\students_data(1).csv")
data=csv.reader(f)
for rec in data:
    for i in data:
        if i[0] not in student:
            student[i[0]]=[int(i[-1])]
        else:
            student[i[0]].append(int(i[-1]))
    

    
# f.close()
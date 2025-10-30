import csv


# faculty_data = []
students_data = []
sub_dic = {}
fac_dic = {}

f = open (':\\Users\\LENOVO\\OneDrive\\Documents\\faculties_data(1) gen ai.csv')
_data = csv.reader(f)
for rec in _data:
#     faculty_data.append(rec)
#     print(rec)
    fac_dic[rec[0]] = rec[1]
f.close()

f_one = open(':\\Users\\LENOVO\\OneDrive\\Documents\\students_data(1).csv')
_data = csv.reader(f_one)
for rec in _data:
    students_data.append(rec)
#     print(rec)
f_one.close()

for rec_one in students_data:
    if int(rec_one[-1]) <= 40:
        if rec_one[1] not in sub_dic:
            sub_dic[rec_one[1]] = 1
#             sub_dic = {'MAths': 1, 'Physics': 1}
        else:
            sub_dic[rec_one[1]] += 1
#             sub_dic = {'MAths': 4, 'Physics': 3}

# print(sub_dic)
# print(fac_dic)
# max(sub_dic.)
fac_dic[min(sub_dic.items(), key=lambda x: x[1])[0]]

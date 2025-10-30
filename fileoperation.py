import csv
import pprint
with open("c:\\Users\\LENOVO\\Downloads\\student_marks.csv") as f:
    data=csv.reader(f)
    act_data=list(data)
# print(act_data)
# s=set()
# for i in act_data[1:]:
#     s.add(i[1])
# pprint.pprint(s)


# d = {}
# for i in act_data[1:]:
#     if i[1] not in d:
#         d[i[1]] = [float(i[3])]  
#     else:
#         d[i[1]].append(float(i[3]))
# print(d)

# d={}
# for i in act_data:
#     if i[1] not in d:
#         d[i[1]]=({i[2]:i[3]})
#     else:
#          d[i[1]].update(({i[2]:i[3]}))

# print(d)



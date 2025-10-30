emp_rec=[('nick',41,5,'microsoft',True),
        ('mike',43,4,'ubisoft',False),
        ('stve',44,2,'ubisoft',False),
        ('dave',45,3,'Microsoft',False),
        ('dave',45,3,'miCrosoft',False),
        ]

# print(max(emp_rec))
# (max(emp_rec,key=lambda x:x[2][2]))
# min_exp=min(emp_rec,key=lambda x:x[1])[1]
# for rec in emp_rec:
#     if rec[1]==min_exp:
#         print(rec)

# emp_rec.sort(key=lambda x:x[2],reverse=True)
# print(emp_rec)

for rec in emp_rec:
    if rec[1]>40 and rec[3].lower()=="microsoft" or rec[3]=="ubisoft":
        print(rec)


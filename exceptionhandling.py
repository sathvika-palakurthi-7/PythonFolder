import json



try:
    f=open("c:\\Users\\LENOVO\\Downloads\\menu_items.json")
    data=json.load(f)
except FileNotFoundError:
    print("file not found")
else:
    print(data)



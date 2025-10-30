import json
f=open("c:\\Users\\LENOVO\\Downloads\\menu_items.json")
data=json.load(f)
# print(menu_data)

# 2. Find All Appetizers 
# Extract and print the name of every menu item that belongs to the "Appetizers" category. 
# appetizers=[]
# for i in data:
#     if i["name"].lower() == "appetizers":
#         # appitizer.append(i)
#         if i["menuItems"]:
#             for apt in i['menuItems']:
#                 appetizers.append(apt["name"])
#                 print(apt['name'])



# 3. Calculate the Average Price of a Beverage 
# Iterate through all non-alcoholic beverages and calculate their average price. The price can 
# be found under customConfigs as itemPrice. 

# Non_Alcoholic_Beverages=[]
# for B in data:
#     if B["name"]=="Beverages":
#         for items in B["subCategories"]:
#             if items["name"]=="Non Alcoholic Beverages":
#                  for k in items["menuItems"]:
#                       Non_Alcoholic_Beverages.append(k['customConfigs'][0]["itemPrice"])
                    
# avg=sum(Non_Alcoholic_Beverages)/len(Non_Alcoholic_Beverages)
# print(avg)
#                 

#   4. Find Items with Multiple Sizes 
# Some menu items, like "Chkn Tender Bskt," come in different sizes (e.g., "SM" and "LG"). Write 
# a script to find and print the name of all items that have more than one size option in their 
# customConfigs. 
                      
# for i in data:
#     if i['menuItems']:
#         for j in i["menuItems"]:
#             # print(j)
#             if j['menuItems']:
#                 for k in j['menuItems']:
#                     if k["customConfigs"] and len(k["customConfigs"]) > 1:       
#                         print(i["name"])
# for output  we need to use nd iterate through the menuItems 

        
# 5. List All Wing Flavors 
# The "Chicken Wings" item has several flavor options. Extract and print the name of each 
# "Wing Flavor" available. 
# for i in data:
#      if i["menuItems"]:
#           for chicken in i["menuItems"]:
#             if chicken["customConfigs"]:
#                 for fla in chicken["customConfigs"]: 
#                     for j in fla["mandatoryModifiers"]:
#                              if j["name"]=="Wing Flavor":
#                                 for k in j["modifiers"]:
#                                      print(k["name"])


#  6. Identify Items with Mandatory Modifiers 
# Some menu items require the customer to make a choice (e.g., a dipping sauce). Find and 
# print the name of all menu items that have at least one mandatory modifier. 
# for i in data:
#      if i["menuItems"]:  
#            for k in i["menuItems"]:
#                 for j in k["customConfigs"]:
#                     if len(j["mandatoryModifiers"])>=1:
#                         print(k["name"])   


# 7. Count the Number of Salads 
# Count and print the total number of unique menu items available in the "Salads & Soups" 
# category. 
# Salads_Soup=[]
# for i in data:
#     if i["menuItems"]:   
#         for j in i["menuItems"]:
#             if j["name"]=="Salads & Soups":
#                      for Salads_Soups in j["name"]:
#                             if Salads_Soups  not in j["menuItems"]:
#                                 Salads_Soup.append(Salads_Soups["menuItems"])
# print(len(Salads_Soup))
# s = set()
# for i in data:
#     if i['name'] == 'Salads & Soups':
#         if i['menuItems']:
#             for _name in i['menuItems']:
#                 s.add(_name['name'])
# print(s)

# 8.Find the Most Expensive Item 
#   Iterate through all menu items across all categories and find the one with the highest   
# max_price={}
# for i in data:
#     if i["menuItems"]:
#         for j in i["menuItems"]:
#             print(j['name'], j['customConfigs'][])

            # if j["customConfigs"]:
            #     for k in j["customConfigs"]:
            #         max_price[k['name']] = k["itemPrice"]
# print(max_price)










        
# 10. Create a Simple Menu Dictionary 
# Write a script to transform the JSON data into a simpler dictionary where the keys are the 
# main category names (e.g., "Appetizers," "Beverages") and the values are a list of the menu 
# item names in that category. Print the resulting dictionary.

# menu={}
# for items in data:
#      if items["menuItems"]:
#          for item_name in items["menuItems"]:
#              if items["name"] not in menu:
#                  menu[items["name"]]=[item_name["name"]]
#              else:
#                  menu[items["name"]].append(item_name["name"])
# print(menu)


        

            




            
            



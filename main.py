import json
from dummy_data import data1
# ----------------- Global Variables -------------------------------------------
global session_data

# ----------------- Classes ----------------------------------------------------
class Shirt:
    def __init__(self,index,name):
        self.index = index
        self.name = name
    # def __repr__(self):
    #     return f"index: {self.index} \n Name: {self.name}"
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    pass
# /------------------------------- Test Data -------------------------------------
# data1 = {
#     "shirt_1":{
#         "index":1,
#         "name":"The Marshal Lee"
#     },
#     "shirt_2":{
#         "index":2,
#         "name":"The Lumbo-Jack"
#     }
# }
# session_data="Hello"
# with open("./data_file.json","w") as test_file:
#     json.dump(data1, test_file)
    

# with open("./data_file.json","w") as test_file:
#     json.dump(data, test_file)
    
# with open("./data_file.json","r") as test_file:
#     print(test_file.read())

# -------------------- Store dictionary's object  -------------------------------------------- 
def obj_to_dict(obj):
    return obj.__dict__


# -------------------- Load and Parse JSON data ------------------------------------------------
def display_shirts_file_in_terminal():
    with open("./data_file.json","r") as test_file:
        json_string=json.load(test_file)
        data = json.loads(json_string)
        return data
        # return sess
#  ************************ -Session Data- *****************************************************
# TODO - Convert Session Data into an object that can hold a list, and a formatting for presenting it in the terimnal, keep it simple
try:
    session_data = display_shirts_file_in_terminal()
except:
    session_data =[]
#  ************************ CRUD Functions *****************************************************
# ----------- Create new entry ------------------
def add_entry(shirt):
    # entry = Shirt(shirt,0)
    entry = Shirt(len(session_data)+1,shirt)
    session_data.append(entry)
    pass

# /---------- Remove a Shirt ------------
def remove_entry():
    print("Removing Entry")
    pass
# /---------- Update a Shirt ------------
def update_entry():
    print("Updating Entry")
    pass
#Update existing Shirt by overwriting 
def update_entry(entry):
    with open("./data_file.json","w") as test_file:
        json.dump(entry, test_file)
        # json.dumps(entry)
# update_entry(session_data)

# ------------ Convert Session Data -> JSON Data -----------------  


# add_entry("The Lumbo-Jack")
# add_entry("The Marshal Lee")
# add_entry("Arbo Swamp")
# add_entry("Midnight Hawaiian")
# add_entry("Sage Green")

json_string = json.dumps(session_data,default=obj_to_dict)
update_entry(json_string)
# print(session_data)
# print(session_data[0])
# Kee

# -------------------------------------------------------------------------------------------------------------------------------

# Controls - Interactive part of program that allows for the CRUD Operations of the program
def user_decisions(selection):
    selection=selection.lower()
    print(selection)
    if selection=="see inventory":
        print("Getting Inventory")
        print(session_data)
    elif selection=="add an item":
        print("Adding entry!")
        shirt_entry = input("Add Entry: ") 
        add_entry(shirt_entry)
# ---------Will involve a selection function------------
    elif selection=="update an item":
        print("Updating entry!")
        update_entry()
    elif selection=="delete an item":
        print("Deleting entry!")
        remove_entry()
        # ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦ Exit Function♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
    elif selection=="exit":
        print("quitting")
        return "quit" #Quits the function
    else:
        print("\nUnfortunately that is not an option. \n\n  ¯\_(ツ)_/¯ \n\n")
    terminal_menu()

# ---------------Session Data Selector---------------
def select_entry_in_session_data(selected_entry):
    print(selected_entry)
    pass
    # return options[selection]
def terminal_menu():
    print("Main Menu")
    print(" + See Inventory \n + Add an Item \n + Update an Item \n + Delete an Item\n + Exit")
    user_input = input("Select an option: ")
    user_decisions(user_input)

# Test
terminal_menu()
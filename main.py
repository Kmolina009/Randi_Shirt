import json
from dummy_data import data1
# ----------------- Global Variables -------------------------------------------
global session_data

# ----------------- Classes ----------------------------------------------------
class Shirt:
    def __init__(self,index,name):
        self.index = index
        self.name = name
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    pass

# -------------------- Store dictionary's object  -------------------------------------------- 
def obj_to_dict(obj):
    return obj.__dict__

# -------------------- Load and Parse JSON data ------------------------------------------------
def display_shirts_file_in_terminal():
    with open("./data_file.json","r") as test_file:
        json_string=json.load(test_file)
        data = json.loads(json_string)
        return data
#  ************************ -Session Data- *****************************************************
try:
    session_data = display_shirts_file_in_terminal()
except:
    session_data =[]
#  ************************ CRUD Functions *****************************************************
# ----------- Create new entry ------------------
def add_entry(shirt):
    entry = Shirt(len(session_data)+1,shirt)
    session_data.append(entry)
    pass

# /---------- Remove a Shirt ------------
def remove_entry():
    print("Removing Entry")
    pass
# /---------- Update a Shirt ------------
def update_item(shirt):
    select_entry_by_name(shirt)
    pass
#Update existing Shirt by overwriting 
def update_entry(entry):
    with open("./data_file.json","w") as test_file:
        json.dump(entry, test_file)

# ------------ Convert Session Data -> JSON Data -----------------  


json_string = json.dumps(session_data,default=obj_to_dict)
update_entry(json_string)

# ------------ Entry Selection Control -----------------
def select_entry_by_name(entry_name):
    matched_entry = ""
    for entry in session_data:
        if entry["name"] == entry_name:
            print("Item Found!")
            matched_entry = entry
            break
        else:
            print("This item does not exist\n Would you like to add it? ")
            pass
    print(matched_entry)
    matched_entry["name"]=input("What would you like to change the name of your entry to? ")
    print(matched_entry)
    pass

def select_entry_by_number():
    pass
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
        entry_to_update = input("Which entry would you like to update?")
        print("Updating entry!\n")
        # Create a function that determines whether a number or string is being passed
        # TODO Have the function retrive the entry for modification
        update_item(entry_to_update)
        # Pass to function that displays updated entry with the rest
        print(session_data)
    elif selection=="delete an item":
        entry_to_delete = input("Which entry would you like to update?")
        print("Deleting entry!")
        remove_entry() # Take entry as a parameter
        # Remove Function take an entry - checks the session_data list for a matching name -> Removes match
        # ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦ Exit Function♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
    elif selection=="exit":
        print("Exiting")
        return "Exit Successful"
    else:
        print("\nUnfortunately that is not an option. \n\n  ¯\_(ツ)_/¯ \n\n")
    terminal_menu()
    
# ---------------Session Data Selector---------------
def select_entry_in_session_data(selected_entry):
    print(selected_entry)
    pass

def terminal_menu():
    print("Main Menu")
    print(" + See Inventory \n + Add an Item \n + Update an Item \n + Delete an Item\n + Exit")
    user_input = input("Select an option: ")
    user_decisions(user_input)

# Test
terminal_menu()
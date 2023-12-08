from todo_functions import add_todo, remove_todo, mark_todo, view_todo

file_name = "list.csv"

try:
    # open the file in read mode
    todo_file = open(file_name, "r") 
    todo_file.close()
    print("In try block")
    # if it throws error, it means the file doesn't exist
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    todo_file = open(file_name, "w")
    # We can also insert the first line into the file
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

print("Welcome to your To-Do list!")

def create_menu(): #creating a function
    print("1. Enter 1 to add item to your list")
    print("2. Enter 2 to remove item to  your list")
    print("3. Enter 3 to mark an item as completed")
    print("4. Enter 4 to view your todo list")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ") #saves the input into the Choice variable
    return choice

users_choice = "" #This is a global variable to take the Choice value

while users_choice != "5": #As long as the choice is not 5, run the above 5 options
    users_choice = create_menu() #if the user's input is one of the items from the 5 menus above
    if (users_choice == "1"):
        add_todo(file_name)
    elif (users_choice == "2"):
        remove_todo(file_name)
    elif (users_choice == "3"):
        mark_todo(file_name)
    elif (users_choice == "4"):
        view_todo(file_name)
    elif (users_choice == "5"):
        continue #skip to the last step and not the next line
    else:
        print("Invalid input!")

print("Thank you for using the todo list!")
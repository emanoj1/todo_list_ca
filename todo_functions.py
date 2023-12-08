import csv

def add_todo(file_name):
    print("Add add todo")
    # Ask the title of the todo
    todo_name = input("Enter a todo: ")
    # Open file: list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f) #writer is an object
        # Insert values: title = user entered
                    # completed = False
        writer.writerow([todo_name, "False"]) 

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Remove Mark")

def view_todo(file_name):
    print("Remove view")
    
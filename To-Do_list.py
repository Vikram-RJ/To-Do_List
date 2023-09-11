print("\n***** Welcome to Vikram's To-Do List Program *****\n")
category_count= int(input("On how many categories you are going to divide your To-Do things : "))
print()
todo_list = {}
for i in range(category_count):
    print("Enter category",i+1,": ", end= '')
    todo_list[input()] = []

def categories_options():
    categories = list(todo_list.keys())
    print("\nList of all categories : ")
    for i in range(len(todo_list)):
        print(str(i+1)+")", categories[i])
    print("\nEnter - ", end= '')
    for i in range(len(todo_list)):
        print(i+1,"for",categories[i])
    print(len(todo_list)+1,"for Back to main options")

def main_options():
    print("""
Enter - 1 for Add a new category
2 for Delete a category
3 for List of Categories and some functions
4 for Show all categories and to-do things
5 for Exit Vikram's To-Do List Program
          """)

def todo_options(n):
    values = list(todo_list.values())
    if values[n-1] == []:
        print("\n* There is No To-Do thing in this category! *")
    else:
        print()
        for i in range(len(values[n-1])):
            print("-",values[n-1][i])

def sub_options():
    print("""
Enter - 1 for Add a new To-Do thing
2 for Delete a To-Do thing
3 for Back to main options
          """)

def show_all():
    print("\n*** Displaying all the To-Do things with their Categories! ***")
    keys = list(todo_list.keys())
    values = list(todo_list.values())
    for i in range(len(todo_list)):
        print("\n"+keys[i]+" : ")
        if values[i] != []:
            for j in range(len(values[i])):
                print("     - "+str(values[i][j]))

def add_category():
    todo_list[input("\nEnter the name of the category you wanted : ")] = []
    print("Successfully Added!")

def delete_category():
    keys = list(todo_list.keys())
    category = input("Enter the category name that you want to Delete : ")
    if category in keys:
        del todo_list[category]
        print("Successfully Deleted!")
    else:
        print("\n* The category you want to delete is actually not in the category list! *")
    
def add_todo(n):
    keys = list(todo_list.keys())
    values = list(todo_list.values())
    find = keys[n-1]
    thing = input("Enter a new to-do thing : ")
    add = []
    if values[n-1] != []:
        for i in range(len(values[n-1])):
            add.append(values[n-1][i])
    add.append(thing)
    todo_list[find] = add
    print("Successfully Added!")

def delete_todo(n):
    keys = list(todo_list.keys())
    values = list(todo_list.values())
    find = keys[n-1]
    if values[n-1] == []:
        print("\n* There is Nothing to Delete! *")
    else:
        thing = input("Enter the to-do thing you want to delete : ")
        if thing in values[n-1]:
            add = []
            for i in range(len(values[n-1])):
                add.append(values[n-1][i])
            add.remove(thing)
            todo_list[find] = add
            print("Successfully Deleted!")
        else:
            print("\n* The To-Do thing you want to delete is actually not in the To-Do List! *")

while(True):
    main_options()
    main_option = int(input("Enter the option : "))
    if main_option == 1:
        add_category()

    elif main_option == 2:
        delete_category()
    
    elif main_option == 3:
        categories_options()
        categories_option = int(input("Enter the option : "))
        if categories_option <= len(todo_list):
            todo_options(categories_option)
            sub_options()
            sub_option = int(input("Enter the option : "))
            if sub_option == 1:
                add_todo(categories_option)
            
            elif sub_option == 2:
                delete_todo(categories_option)

            elif sub_option == 3:
                pass
            
            else:
                print("*** You have entered a wrong option, kindly enter a correct option! ***")
        
        elif categories_option == len(todo_list)+1:
            main_options()
        
        else:
            print("*** You have entered a wrong option, kindly enter a correct option! ***")
    
    elif main_option == 4:
        show_all()
    
    elif main_option == 5:
        print("\n***** Thanks for using Vikram's To-Do List Program! Visit Again! *****\n")
        break

    else:
        print("*** You have entered a wrong option, kindly enter a correct option! ***")

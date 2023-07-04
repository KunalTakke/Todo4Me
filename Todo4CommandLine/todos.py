# import os # for storing the todos in a file system
from colorama import Back,Fore,Style # color library

# defining the functions for adding,deleting,editing and printing the todos
def add_todo():
    todos=[] # initialize an empty list
    todo=input("Enter the Todo to be added :")
    # read all todos till we reach the end of the file
    with open("Todos.txt","r") as f:
        todos=f.readlines()
    # test case 1:check if the same todo exists in the list or not
    # add new todo as a string
    todos.append(todo+"\n")
    with open("Todos.txt","w") as f:
        for t in todos:
            f.writelines(t)
    print()
    print(Fore.GREEN+"Operation Completed: Added a new todo")
    print(Style.RESET_ALL)

def delete_todo():
    todos=[]
    todo=int(input("Enter the todo item number to be deleted :"))
    try:
        with open("Todos.txt", "r") as f:
            todos = f.readlines()
        actual=todo-1
        if(actual<0 or actual>=len(todos)):
            print("Invalid number given")
        else:
            todos.pop(todo - 1)
        with open("Todos.txt", "w") as f:
            for t in todos:
                f.writelines(t)
    except:
        print("Invalid number given, plz check the todo number")




def edit_todo():
    pass

def print_todo():
    todo=[]
    with open("Todos.txt","r") as f:
        todo=f.readlines()
    print(f"The todo as a list is {todo}")
    print(f"the length of the todo is {len(todo)}")
    # print the todo
    for t in todo:
        print(f"{todo.index(t)+1}.{t}")



if __name__=="__main__":
    while True:
        print(Fore.GREEN+"######################################")
        print("   Welcome to Todo4CommandLine")
        print("######################################")
        print(Style.RESET_ALL) # reset the color scheme
        print()
        print("**************MENU**************")
        print("Select the operations by number: ")
        print("1. Add Todo")
        print("2. Delete todo ")
        print("3. Edit existing todo")
        print("4. Print the Todos")
        print("5. Close/Exit ")
        query=input("Enter the operation number to be performed: ")
        query=int(query.strip()) # strip the spaces and convert into int
        if query==1:
            # call add_todo
            add_todo()
        elif query==2:
            # call delete_todo
            delete_todo()
        elif query==3:
            # call edit_todo
            edit_todo()
            pass
        elif query==4:
            print_todo()
        elif query==5:
            print("Bye :)")
            break
        else:
            # default 
            print(Fore.RED+"Please Enter a valid operation number")
            print(Style.RESET_ALL)
            continue



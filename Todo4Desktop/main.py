import tkinter
from tkinter import *
from tkinter import ttk

# tkinter._test()
root = Tk()
root.title("Todo4Me")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Welcome to Todo4Me !").grid(column=0, row=0)
# use next line here

# when you click add button it will trigger the add todo function
# add todo entry here !
task_name=StringVar()
new_todo=ttk.Entry(frm,textvariable=task_name,width=75).grid(column=0,row=1)

def demo_input():
    print(task_name.get())
# ttk.Button(frm, text="dd", command=demo_input).grid(column=3, row=2)

# function for adding new todo
def add_todo():
    # first take it in todo
    # print(task_name.get())
    todos=[] # initialized a list
    with open("Todos.txt","r") as f:
        todos=f.readlines()

    # add the task
    print(f"task_name is {task_name.get()}")
    todos.append(task_name.get()+"\n")
    print(todos)
    # commit the todo into text file
    with open("Todos.txt","w") as f:
        for todo in todos:
            f.writelines(todo)

    print_todo()


add_todo_button=ttk.Button(frm, text="Add todo", command=add_todo).grid(column=2, row=1)

# fetch todos/ print todos
def print_todo():
    todos = []  # initialize an empty list
    with open("Todos.txt","r") as f:
        todos=f.readlines()
    # print todos
    for items in todos:
        ttk.Label(text=f"{todos.index(items)+1}. {items}").grid(column=1,row=todos.index(items)+1)
        # ttk.Button(frm, text="Delete Todo", command=root.destroy).grid(column=2, row=todos.index(items)+1)


def delete_todo():
    print("Delete button")

ttk.Button(frm,command=delete_todo)


def edit_todo():
    print("Edit button")

ttk.Button(frm,command=edit_todo)



print_todo()
root.mainloop()






#
# ttk.Button(frm, text="Delete Todo", command=root.destroy).grid(column=2, row=2)
# ttk.Button(frm, text="Edit", command=root.destroy).grid(column=3, row=2)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=2)
#
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=12)







print("welcome to the to do list app!")
print("your to do list:")
tasks = []
checked = []
def listdisplay():
    print(tasks)
print("1: add task\n2: display tasks\n3: remove a task\n4: check off a task\n5: see completed tasks\n6: exit")
options = input("\nchoose an option:")
while options == "1" or options == "2" or options == "3" or options == "4" or options =="5":
    if options == "1":
        newtask = input("add a task:")
        tasks.append(newtask)
        for task in tasks:
            print(task)
    if options == "2":
        if len(tasks) == 0:
            print("your list is empty!")
        for task in tasks:
            print(task)
    if options == "3":
        removetask = input("which task do you want to remove?")
        tasks.remove(removetask)
        for task in tasks:
            print(task)
    if options == "4":
         completed = input("which task do you want to check off?")
         tasks.remove(completed)
         checked.append(completed)
         for task in tasks:
            print(task)
    if options =="5":
        print(checked)
        for task in tasks:
            print(task)

    options = input("choose an option:")
print("goodbye!")
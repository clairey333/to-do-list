print("welcome to the to do list app!")
print("your to do list:")
tasks = []
def listdisplay():
    print(tasks)
print("1: add task\n2: display tasks\n3: remove\n4: exit")
options = input("\nchoose an option:")
while options == "1" or options == "2" or options == "3":
    if options == "1":
        newtask = input("add a task:")
        tasks.append(newtask)
        print(tasks)
    if options == "2":
        if len(tasks) == 0:
            print("your list is empty!")
        for task in tasks:
            print(task)
    if options == "3":
        removetask = int(input("which task do you want to remove?"))
        
    options = input("choose an option:")
print("goodbye!")

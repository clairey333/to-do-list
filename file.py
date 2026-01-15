print("welcome to the to do list app!")
print("your to do list:")
tasks = ["play tennis, cook food, study for midterms, code"]
def listdisplay():
    print(tasks)
print("1: add task\n2: display tasks\n3: exit")
options = input("\nchoose an option:")
while options == "1" or options == "2":
    if options == "1":
        newtask = input("add a task:")
        tasks.append(newtask)
        print(tasks)
    options = input("choose an option:")

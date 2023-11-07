tasks=[]
def add_task(task):
    tasks.append(task)
    print("Task " +task+ " added to the to-do list: ")
def view_task():
    if not tasks:
        print("No tasks in the to-do list")
    else:
        print("To-do list: ")
    print(tasks)
def remove_task(index):
    if 1<=index<=len(tasks):
        removed_task=tasks.pop(index-1)
        print("Task " + removed_task + " removed from the to-do list.")
while True:
    print("\nOptions:")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove a task")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task=str(input("Enter the task: "))
        add_task(task)
    elif choice==2:
        view_task()
    elif choice==3:
        view_task()
        index=int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice==4:
        break
    else:
        print("Invalid choice. Please enter valid choice")
        
                 
               

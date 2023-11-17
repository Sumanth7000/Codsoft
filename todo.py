todo_list = []

while True:
    print("\nSimple Todo List")
    print("1. Adding tasks to the list")
    print("2. Viewing tasks in the list")
    print("3. Removing tasks from the list")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        task = input("Enter your task: ")
        todo_list.append(task)
        print(f"'{task}' has been added to the list.")

    elif option == "2":
        print("\nTasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

    elif option == "3":
        task = input("Enter the task you want to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print(f"'{task}' has been removed from the list.")
        else:
            print(f"'{task}' isn't in the list.")

    elif option == "4":
        break

    else:
        print("Invalid input. Please enter a number between 1 and 4.")

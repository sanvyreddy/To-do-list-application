#Define an empty list to store tasks
tasks = []

#function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")
          
#Function to add a task to the to-do list
def add_task():
    task = input("Enter a new task:")
    tasks.append(task)
    print("Task added successfully.")

#Function to mark a task as completed
def mark_completed():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print('List of tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

        choice = int(input('Enter the task number to mark as completed:'))

        if 0 < choice <= len(tasks):
            # You can add some logic here to mark the task as completed
            print(f'Task {choice} marked as completed.')
        else:
            print('Invalid task number.')

#Function to remove a task from the to-do list
def remove_task():
    if len(tasks) == 0:
        print('No task to remove.')
    else:
        print('Current tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        
        choice = int(input('Enter the task number to remove:'))
        
        if 0 < choice <= len(tasks):
            removed_task = tasks.pop(choice-1)
            print(f'Task "{removed_task}" removed successfully.')
        else:
            print('Invalid task number.')
            
#Main program loop
while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            mark_completed()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            print("Thank you for using the To-Do-List Application.")
            break
        else:
            print("Invalid choice. please try again.")





    
    

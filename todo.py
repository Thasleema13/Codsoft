#TO DO list

tasks = []

def add_task(description):
  global tasks
  task_id = len(tasks) + 1
  tasks.append({'id': task_id, 'description': description, 'status': 'incomplete'})
  print("Task",description, "added")

def view_tasks():
  if not tasks:
    print("No tasks found.")
  else:
    print("To-Do List:")
    for task in tasks:
      status = "Completed" if task['status'] == 'completed' else "Incomplete"
      print(f"{task['id']}. {task['description']} - {status}")

def mark_completed(task_id):
  for task in tasks:
    if task['id'] == task_id:
      task['status'] = 'completed'
      print(f"Task {task_id} marked as completed.")
      return
  print("Task with ID ",task_id," not found.")

def delete_task(task_id):
  for i, task in enumerate(tasks):
    if task['id'] == task_id:
      del tasks[i]
      print("Task ",task_id,"deleted.")
      return
  print("Task with ID",task_id, "not found.")

def edit_task(task_id):
 
  for task in tasks:
    if task['id'] == task_id:
      new_description = input("Enter new description: ")
      task['description'] = new_description
      print("Task",task_id,"updated.")
      return
  print("Task with ID", task_id,"not found.")

while True:
  print("To-Do List")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark as Completed")
  print("4. Delete Task")
  print("5. Edit Task")
  print("6. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    description = input("Enter task description: ")
    add_task(description)
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    try:
      task_id = int(input("Enter task ID: "))
      mark_completed(task_id)
    except ValueError:
      print("Invalid input for task ID.") 
  elif choice == '4':
    try:
      task_id = int(input("Enter task ID: "))
      delete_task(task_id)
    except ValueError:
      print("Invalid input for task ID.")
  elif choice == '5':
    try:
      task_id = int(input("Enter task ID: "))
      edit_task(task_id)
    except ValueError:
      print("Invalid input for task ID.")
  elif choice == '6':
    print("Exiting...")
    break
  else:
    print("Invalid choice.")

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.description} - Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")

    def mark_task_completed(self, task_index):
        task = self.tasks.pop(task_index - 1)
        task.completed = True
        self.completed_tasks.append(task)

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        task = self.tasks[task_index - 1]
        task.description = new_description
        task.due_date = new_due_date
        task.priority = new_priority

    def remove_task(self, task_index):
        del self.tasks[task_index - 1]

# Example Usage
todo_list = ToDoList()

task1 = Task("Complete project", "2023-11-15", "High")
task2 = Task("Buy groceries", "2023-11-12", "Medium")

todo_list.add_task(task1)
todo_list.add_task(task2)

todo_list.display_tasks()

todo_list.mark_task_completed(1)
todo_list.display_tasks()

todo_list.update_task(2, "Buy weekly groceries", "2023-11-13", "Medium")
todo_list.display_tasks()

todo_list.remove_task(1)
todo_list.display_tasks()

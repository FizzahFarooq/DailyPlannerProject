import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, duration, priority, description):
        self.name = name
        # (in minutes)
        self.duration = duration 
        # (1: High, 2: Medium, 3: Low) 
        self.priority = priority  
        self.description = description
        # New attribute to track completion
        self.is_complete = False  

    def __str__(self):
        status = "Complete" if self.is_complete else "Incomplete"
        return f"{self.name} (Priority {self.priority}) - {self.duration} min - {status}"


# Create the main window with gray background
root = tk.Tk()
root.title("Personalized Daily Planner")
root.geometry("600x600")
root.configure(bg="#808080")  

task_list = []

# Function to create a task and add it to the task list
def add_task():
    name = entry_name.get()
    try:
        duration = int(entry_duration.get())
        priority = int(entry_priority.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for duration and priority.")
        return
    description = entry_description.get()
    task = Task(name, duration, priority, description)
    task_list.append(task)
    entry_name.delete(0, tk.END)
    entry_duration.delete(0, tk.END)
    entry_priority.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    update_task_listbox()
    messagebox.showinfo("Task Added", f"Task '{task.name}' added to the planner.")

# Function to update the task listbox
def update_task_listbox():
    listbox.delete(0, tk.END)
    for task in task_list:
        listbox.insert(tk.END, f"{task.name} (Priority {task.priority}) - {task.duration} min - {'Complete' if task.is_complete else 'Incomplete'}")

# Function to mark a task as complete
def mark_task_complete():
    selected_task_index = listbox.curselection()
    if not selected_task_index:
        messagebox.showerror("Error", "Please select a task to mark as complete.")
        return
    selected_task = task_list[selected_task_index[0]]
    if selected_task.is_complete:
        messagebox.showinfo("Already Complete", f"The task '{selected_task.name}' is already marked as complete.")
    else:
        selected_task.is_complete = True
        update_task_listbox()
        messagebox.showinfo("Task Completed", f"Task '{selected_task.name}' has been marked as complete.")

# Function to show task details
def show_task_schedule():
    schedule_message = "Task Schedule:\n\n"
    for task in task_list:
        schedule_message += f"Name: {task.name}\n"
        schedule_message += f"Duration: {task.duration} min\n"
        schedule_message += f"Priority: {task.priority}\n"
        schedule_message += f"Description: {task.description}\n"
        schedule_message += f"Status: {'Complete' if task.is_complete else 'Incomplete'}\n\n"
    
    if not task_list:
        schedule_message = "No tasks available."
    
    messagebox.showinfo("Task Schedule", schedule_message)

# GUI 
frame = tk.Frame(root, bg="#808080")
frame.pack(pady=20)

label_name = tk.Label(frame, text="Task Name:", font=("Arial", 14), bg="#808080", fg="black")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame, font=("Arial", 14), width=30)
entry_name.grid(row=0, column=1)

label_duration = tk.Label(frame, text="Duration (min):", font=("Arial", 14), bg="#808080", fg="black")
label_duration.grid(row=1, column=0, padx=10, pady=5)
entry_duration = tk.Entry(frame, font=("Arial", 14), width=30)
entry_duration.grid(row=1, column=1)

label_priority = tk.Label(frame, text="Priority (1-High, 2-Medium, 3-Low):", font=("Arial", 14), bg="#808080", fg="black")
label_priority.grid(row=2, column=0, padx=10, pady=5)
entry_priority = tk.Entry(frame, font=("Arial", 14), width=30)
entry_priority.grid(row=2, column=1)

label_description = tk.Label(frame, text="Description:", font=("Arial", 14), bg="#808080", fg="black")
label_description.grid(row=3, column=0, padx=10, pady=5)
entry_description = tk.Entry(frame, font=("Arial", 14), width=30)
entry_description.grid(row=3, column=1)

# Buttons
button_add = tk.Button(root, text="Add Task", font=("Arial", 14), bg="#C085A1", fg="black", command=add_task)
button_add.pack(pady=10)



button_schedule = tk.Button(root, text="Show Task Schedule", font=("Arial", 14), bg="#FFD740", fg="black", command=show_task_schedule)
button_schedule.pack(pady=10)

button_mark_complete = tk.Button(root, text="Mark Task as Complete", font=("Arial", 14), bg="#00E676", fg="black", command=mark_task_complete)
button_mark_complete.pack(pady=10)

listbox = tk.Listbox(root, font=("Arial", 14), width=50, height=10)
listbox.pack(pady=20)

root.mainloop()

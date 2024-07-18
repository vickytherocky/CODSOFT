import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import filedialog
tasks = []
def add_task():
    new_task = simpledialog.askstring("Add Task", "Enter a new task:")
    if new_task:
        tasks.append(new_task)
        update_task_list()
        messagebox.showinfo("Task Added", f"Task '{new_task}' added successfully!")

def view_tasks():
    update_task_list()

def mark_task_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        completed_task = tasks.pop(task_index)
        update_task_list()
        messagebox.showinfo("Task Completed", f"Task '{completed_task}' marked as done!")
    else:
        messagebox.showwarning("No Selection", "Please select a task to mark as done.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x300")
root.config(bg="#f0f0f0")

task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_listbox = tk.Listbox(task_frame, height=10, width=50, bg="#e0e0e0", fg="#333333", selectbackground="#c0c0c0")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="#ffffff", padx=10, pady=5)
add_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(button_frame, text="View Tasks", command=view_tasks, bg="#2196F3", fg="#ffffff", padx=10, pady=5)
view_button.grid(row=0, column=1, padx=5, pady=5)

done_button = tk.Button(button_frame, text="Mark Task Done", command=mark_task_done, bg="#f44336", fg="#ffffff", padx=10, pady=5)
done_button.grid(row=0, column=2, padx=5, pady=5)

quit_button = tk.Button(button_frame, text="Quit", command=root.quit, bg="#795548", fg="#ffffff", padx=10, pady=5)
quit_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

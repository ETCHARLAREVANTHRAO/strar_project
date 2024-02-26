import tkinter as tk
import speech_recognition as sr

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_task():
    day = day_listbox.get(tk.ACTIVE)
    time = time_entry.get()
    task = task_entry.get()
    if day != "" and time != "" and task != "":
        task_list[day].append((time, task))
        task_entry.delete(0, tk.END)

def show_tasks():
    day = day_listbox.get(tk.ACTIVE)
    task_text.delete("1.0", tk.END)
    for task in task_list[day]:
        task_text.insert(tk.END, f"{task[0]}: {task[1]}\n")

def fill_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")

root = tk.Tk()
root.title("Weekly Planner with Voice Input")

task_list = {day: [] for day in weekdays}

day_frame = tk.Frame(root)
day_frame.pack(side=tk.LEFT, padx=10, pady=10)

day_label = tk.Label(day_frame, text="Select a day:")
day_label.pack(side=tk.TOP)

day_listbox = tk.Listbox(day_frame, width=10)
for day in weekdays:
    day_listbox.insert(tk.END, day)
day_listbox.pack(side=tk.TOP)

time_label = tk.Label(day_frame, text="Enter a time:")
time_label.pack(side=tk.TOP, pady=(10, 0))

time_entry = tk.Entry(day_frame)
time_entry.pack(side=tk.TOP)

task_label = tk.Label(day_frame, text="Enter a task:")
task_label.pack(side=tk.TOP, pady=(10, 0))

task_entry = tk.Entry(day_frame)
task_entry.pack(side=tk.TOP)

add_button = tk.Button(day_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.TOP, pady=(10, 0))

show_button = tk.Button(day_frame, text="Show Tasks", command=show_tasks)
show_button.pack(side=tk.TOP, pady=(10, 0))

input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, padx=10, pady=10)

input_label = tk.Label(input_frame, text="Fill task or time with voice command:")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT, padx=5)

input_button = tk.Button(input_frame, text="Record", command=fill_input)
input_button.pack(side=tk.LEFT, padx=5)

task_frame = tk.Frame(root)
task_frame.pack(side=tk.LEFT, padx=10, pady=10)

task_label = tk.Label(task_frame, text="Tasks:")
task_label.pack(side=tk.TOP)

task_text = tk.Text(task_frame, width=40, height=20)
task_text.pack(side=tk.TOP)

root.mainloop()

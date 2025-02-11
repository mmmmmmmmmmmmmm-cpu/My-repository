from tkinter import *
from tkinter import messagebox
import json
zero = 0
y = 120
font = ('Arial', 15, 'bold')
entrys = []
task = 1
tasks = []

if open("day.txt", "r") == True:
    lines = open("day.txt", "r")
    day = lines[-1]
else:
    day = 1


def save():
    global day
    for i in entrys:
        task = i.get()
        tasks.append(task)

    new_data = {
        f"Day {day}": {
            "Task.1": tasks[0],
            "Task.2": tasks[1],
            "Task.3": tasks[2],
            "Task.4": tasks[3],
            "Task.5": tasks[4]
        }
    }
    if len(task) == 0 or len(task) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=5)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=5)
        finally:
            for i in entrys:
                i.delete(0, END)
            day += 1
            with open("day.txt", "w") as w:
                w.write(f"{day}")




window = Tk()
window.config(padx=50, pady=50)
canvas = Canvas(height=300, width=400)
canvas.grid(row=0, column=1)

title = Label(text="TO DO LIST", font=('Arial', 20, 'bold'))
title.place(x=0, y=0)
first = Label(text="1.", font=font)
first.place(x=50, y=40)
second = Label(text="2.", font=font)
second.place(x=50, y=80)
ey = 40
for i in range(5):
    first = Label(text=f"{task}.", font=font)
    first.place(x=50, y=ey)
    entry = Entry(width=40)
    entry.place(x=80, y=ey)
    ey += 40
    task += 1
    entrys.append(entry)



submit_button = Button(text="Submit", command=save)
submit_button.place(x=300, y=0)





window.mainloop()


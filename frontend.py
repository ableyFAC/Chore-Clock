import timer as timer

import tkinter as tk

mainBackgroundColor = "#ABE4EA"

root = tk.Tk()
root.title("Chore Clock")
root.geometry("589x622")
root.config(bg = mainBackgroundColor)
root.resizable(False, False)

lbl = tk.Label(root, text="Chore Clock")
lbl.config(font=("Michroma", 24), bg = mainBackgroundColor, fg= "black")
lbl.grid(row=0, column=0)
lbl.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

frame = tk.Frame(root, width=500, height=500)
frame.grid(row=0, column=0)
frame.place(relx=0.5, rely=0.48, anchor=tk.CENTER)
frame.config(bg = mainBackgroundColor)

paused = False
def pauseTimer():
    global paused
    paused = not paused
    pauseBtn.config(text="Continue" if paused else "Pause")
    if not paused:
        startTimer()

pauseBtn = tk.Button(frame, text="Pause", command=pauseTimer)
pauseBtn.grid(row=3, column=1, padx=5, pady=5)
pauseBtn.config(bg = mainBackgroundColor, fg= "#FF0004", font=("Michroma", 24), width=10, borderwidth = 0)

def reset():
    entryVar.set("00:00")
    entryWidget.config(bg = "white")

resetBtn = tk.Button(frame, text="Reset", command=reset)
resetBtn.grid(row=4, column=1, padx=5, pady=5)
resetBtn.config(bg = mainBackgroundColor, fg="White", font=("Michroma", 24), width=10, borderwidth = 0)

entryVar = tk.StringVar() 
entryVar.set("00:00")
entryWidget = tk.Entry(frame, textvariable=entryVar, justify="center")
entryWidget.grid(row=0, column=1, padx=5, pady=5)
entryWidget.config(font=("Michroma", 24), width=10, bg="white", fg="black")

def startTimer():
    minutes = int(entryVar.get().split(':')[0])
    seconds = int(entryVar.get().split(':')[1])

    countdown(minutes, seconds)

def countdown(minutes, seconds):
    if(minutes == 0 and seconds == 0):
        entryVar.set("Done!!!")
        entryWidget.config(bg="lightgreen")
        
        return
    
    if not paused:
        entryVar.set(f"{minutes:02d}:{seconds:02d}") 
        minutes, seconds = timer.calculateTime(minutes, seconds)
        entryWidget.after(1000, countdown, minutes, seconds)

startBtn = tk.Button(frame, text="Start Timer", command=startTimer)
startBtn.grid(row=2, column=1, padx=5, pady=5)
startBtn.config(bg=mainBackgroundColor, fg="#13A300", font=("Michroma", 24), width=10, borderwidth = 0)

root.mainloop()

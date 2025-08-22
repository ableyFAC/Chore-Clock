import timer as timer

# root 
root = timer.tk.Tk()
root.title("Chore Clock")
root.geometry("500x600")
root.config(bg="lightblue")
root.resizable(False, False)

# label that displays "Chore Clock"
lbl = timer.tk.Label(root, text="Chore Clock")
lbl.config(font=("Times New Roman", 14), bg="white", fg="black")
lbl.grid(row=0, column=0)
lbl.place(relx=0.5, rely=0.3, anchor=timer.tk.CENTER)

# Centers the entry box and button
frame = timer.tk.Frame(root, width=500, height=500)
frame.grid(row=0, column=0)
frame.place(relx=0.5, rely=0.45, anchor=timer.tk.CENTER)
frame.config(bg = "lightblue")

# the box where the user inputs the time
# entry = tk.Entry(frame)
entryVar = timer.tk.StringVar() # this allows the strings to be binded to a widget, and be updated
entryVar.set("00:00")
entryWidget = timer.tk.Entry(frame, textvariable=entryVar, justify="center")
entryWidget.grid(row=0, column=1, padx=5, pady=5)
entryWidget.config(font=("lexend mega", 12), width=10, bg="white", fg="black")

# i want this button to star the timer
def startTimer():
    minutes = int(entryVar.get().split(':')[0])
    seconds = int(entryVar.get().split(':')[1])

    countdown(minutes, seconds)

# pause button
paused = False
def pauseTimer():
    global paused
    paused = not paused
    pauseBtn.config(text="Continue" if paused else "Pause")
    if not paused:
        startTimer()

pauseBtn = timer.tk.Button(frame, text="Pause", command=pauseTimer)
pauseBtn.grid(row=3, column=1, padx=5, pady=5)
pauseBtn.config(bg="pink", fg="black", font=("lexend mega", 12), width=10)

def countdown(minutes, seconds):
    if(minutes == 0 and seconds == 0):
        entryVar.set("Done!!!")
        entryWidget.config(bg="lightgreen")
        return
    if not paused:
        entryVar.set(f"{minutes:02d}:{seconds:02d}") 
        minutes, seconds = timer.calculateTime(minutes, seconds)
        entryWidget.after(1000, countdown, minutes, seconds)

# button that starts the timer
entryBtn = timer.tk.Button(frame, text="Start Timer", command=startTimer)
entryBtn.grid(row=2, column=1, padx=5, pady=5)
entryBtn.config(bg="lightgreen", fg="black", font=("lexend mega", 12), width=10)

root.mainloop()

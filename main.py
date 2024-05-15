import tkinter
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
work_tick_counter=0

# ---------------------------- TIMER RESET ------------------------------- #
#TODO add sounds
#TODO popup mechanism
#TODO RESET on long break
#TODO customise the reset button to adapt to the session duration

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer(duration):
    x = time.time()
    sec=0
    min=0
    time_string = f"{sec}:{min}"
    while True:
        if min==duration:
            print("tim tim")
            break

        y=time.time()
        while True:
            time.sleep(1)
            sec+=1

            # Format the number with leading zeros
            secs = str(sec).zfill(2)
            mins =str(min).zfill(2)


            print(f"{mins} : {secs}")
            if sec==60:
                sec=0
                min+=1
            break
        #if y==x+duration:
         #   print("eyo eya")
#timer(2)
def inverted_timer(duration):
    x = time.time()
    sec=60
    min=duration

    while True:

        y=time.time()
        while True:
            time.sleep(1)
            sec-=1

            # Format the number with leading zeros
            secs = str(sec).zfill(2)
            mins =str(min).zfill(2)
            if sec==0:
                sec=60
                min-=1


            print(f"{mins} : {secs}")
            break
#inverted_timer(2)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
start=0
sec_count=60

def print_out(min_count,secs):
    global start
    min_count=min_count
    if min_count<0:
        call_print()

    if start == 1:
        min_count = 9
        secs=60
        start=0
    min_count1=str(min_count).zfill(2)
    secs1=str(secs).zfill(2)
    Text = f"{min_count1} : {secs1}"
    canvas.itemconfig(time_text, text=Text)

    if secs>0 and min_count>-1:

        window.after(1000,print_out,min_count,secs-1)
    elif secs==0 and min_count>-1:
        secs=60
        min_count-=1
        window.after(1000, print_out,min_count, secs - 1)
def call_print():
    global  reps
    global work_tick_counter
    reps+=1
    #since work will fall on odd numbers and breaks on even numbers
    if reps==8:
        #long break
        print_out(30-1,60)
        timer_label.config(text="Break",fg=RED)

    elif reps%2==0:
        #short break
        canvas.itemconfig(time_text,text="00:00")
        print_out(2-1,10)
        timer_label.config(text="Break",fg=PINK)
    elif reps%2!=0:
        #work
        #increase ticks everytime
        work_tick_counter+=1

        new_ticks="✔"*work_tick_counter
        tick.config(text=new_ticks)
        print_out(2-1,10)
        timer_label.config(text="Work",fg=GREEN)
def call_reset():
    global start
    start = 1



window=tkinter.Tk()
timer_label=tkinter.Label(text="timer",font=(FONT_NAME,40,"bold"))
timer_label.config(fg=GREEN)
timer_label.config(bg=YELLOW)
timer_label.grid(column=2,row=1)
start_button=tkinter.Button(text="start",command=call_print)
start_button.config(bg="white")
start_button.grid(column=1,row=4)
reset_button=tkinter.Button(text="reset",command=call_reset)
reset_button.config(bg="white")
blank=tkinter.Label(text=" ")

blank.config(bg=YELLOW,fg=YELLOW)
blank.grid(row=3,column=2)
reset_button.grid(column=3,row=4)
tick=tkinter.Label(text="✔")
tick.config(bg=YELLOW,fg=GREEN,font=(FONT_NAME,25))
tick.grid(row=4,column=2)
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas =tkinter.Canvas(width=200,height=224)
canvas.config(bg=YELLOW,highlightthickness=0)
img=tkinter.PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=img)
time_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)


window.mainloop()

mport tkinter as tk
import random
import time
import os 
#Adding Classes
class CoolMathsGame:
        def __init__(self,root):
                self.root=root
                self.root.title="Cool Maths Game"
                self.root.geometry="500x500"
                self.root.configure=bg="0352fc"
class CoolMathsGameQuestion:
        def _init(self):
                self.operation('+','-','*','/')
                self.question=""
                self.answer="None"
#Main window
root = tk.Tk()
root.title('Cool Maths Game')
root.geometry('250x250')
#Adding image
bg_canvas=tk.Canvas(root,width=500,height=500)
bg_canvas.pack(fill="both",expand=True)
image_path=tk.PhotoImage(file=r"C:\Users\karti\OneDrive - Lynfield College\3PAD program\futuristic-threshold-with-reflections-on-wall-and-floor-free-video.png")
bg_canvas.create_image(0, 0,anchor="nw", image=image_path)
# Variables to store question details and game state
operator =""
num1 = 0
num2 = 0
score = 0
time_left = 10  # 10 seconds for the timer
timer_running = False

def show_instructions():
    start_button.pack_forget()
    exit_button.pack_forget()
    instructions_frame.pack()

def start_game():
    global timer_running, score, time_left
    instructions_frame.pack_forget() #instruction frame to be removed when game starts
    game_frame.pack()
    score = 0
    time_left = 10
    update_score()
    generate_question()
    start_timer()
   
def generate_question():
    global operator, num1, num2
    operator = random.choice(['+', '-', '*'])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question_label.config(text=f"What is {num1} {operator} {num2}?")
    answer_entry.delete(0, tk.END)
    answer_entry.focus()

def check_answer():
    global operator, num1, num2, score
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")
        return
   
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
   
       
           
           
       
   
    if user_answer == correct_answer:
        result_label.config(text="Correct!")
        score += 1
    else:
        result_label.config(text=f"Wrong! The correct answer was {correct_answer:.2f}")

    update_score()
    generate_question()


def update_score():
    score_label.config(text=f"Score: {score}")

def start_timer():
    global timer_running
    timer_running = True
    update_timer()

def update_timer():
    global time_left, timer_running
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")
        timer_running = False
        save_score()
def submit():
        global score, lives

        if lives == 0:
                messagebox.showerror(message="You are out of lives.")
                return

        try:
                if int(input_var.get()) == answer:
                       score += 1
                       score_Label.config(text=st(score))
                       generate_question()
                else:
                        messagebox.showinfo(message="Wrong")
                        lives -= 1
                        lives_label.config(text=int(lives))
                        generate_question()
        except Exception as e:
                messagebox.showerror(message=e)
def save_score():
        
    with open("score.txt", "w") as file:
        file.write(f"Final Score: {score}\n")

# instructions frame and label
instructions_frame = tk.Frame(root)
instructions_text = tk.Label(instructions_frame, text="You\n"
                                 "You will have 10 seconds timer to answer the question\n"
                                 "The game will ask you basic maths question \n"
                                 "You will have two lives to play the game")
instructions_text.pack(pady=10)


# home screen frame
home_frame = tk.Frame(root)
home_frame.pack(pady=30)

# start button
start_button = tk.Button(home_frame, text='Start', width=20,fg="Green", command=show_instructions)
start_button.pack(padx=50, side=tk.LEFT)

# exit button
exit_button = tk.Button(home_frame, text='Exit', fg="Red",width=20, command=exit)
exit_button.pack(padx=50, side=tk.LEFT)

# back button
start_game_button = tk.Button(instructions_frame, text='Start Game', command=start_game)
start_game_button.pack(pady=10)

# game screen
game_frame = tk.Frame(root)
question_label = tk.Label(game_frame, text="")
question_label.pack(pady=10)

answer_entry = tk.Entry(game_frame)
answer_entry.pack(pady=10)

submit_button = tk.Button(game_frame, text="Submit", command=check_answer)
submit_button.pack(pady=10)

result_label = tk.Label(game_frame, text="")
result_label.pack(pady=10)

score_label = tk.Label(game_frame, text="Score: 0")
score_label.pack(pady=10)

timer_label = tk.Label(game_frame, text="Time Left: 10")
timer_label.pack(pady=10)
#Running the code
if __name__=="_main_":
        root=tk.Tk()
        app=CoolMathsGame(root)
        root.mainloop()

root.mainloop()


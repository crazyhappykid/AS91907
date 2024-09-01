import tkinter as tk
import random
import time
import os
#Main class to hadle the game
class CoolMathsGame:
        def __init__(self,root):
                self.root=root
                self.root.title="Cool Maths Game"
                self.root.geometry="500x500"#Geometry size of the window
                self.root.configure=bg="0352fc"#Background colour for the window
#class for generating questions 
class CoolMathsGameQuestion:
        def _init(self):
                self.operation('+','-','*','/')#Handle the game operations 
                self.question=""
                self.answer="None"
#Main window setup
root = tk.Tk()
root.title('Cool Maths Game')
root.geometry('500x500')
#Adding canvas for the background image
bg_canvas=tk.Canvas(root,width=500,height=500)
bg_canvas.pack(fill="both",expand=True)
#loading the background image 
image_path=tk.PhotoImage(file=r"C:\Users\karti\OneDrive - Lynfield College\3PAD program\futuristic-threshold-with-reflections-on-wall-and-floor-free-video.png")
bg_canvas.create_image(0, 0,anchor="nw", image=image_path)
#creating game frame
game_frame=tk.Frame(bg_canvas,bg="White")
game_frame.pack(padx=20,pady=20)
# Variables to store question details and game state
operator =""#operations used in the game
num1 = 0 #First number
num2 = 0#second numbee
lives= 2 #Lives for the Game
score = 0#score of the game
time_left = 10  # 10 seconds for the timer
timer_running = False #Check if the time is running 
#function to show the instruction of the game
def show_instructions():
    start_button.pack_forget()#Hide start button of the game
    exit_button.pack_forget()#Hide exit button of the Game
    instructions_frame.pack()#Show instruction of the Game
#function to start the Game
def start_game():
    global timer_running, score, time_left,lives
    instructions_frame.pack_forget() #instruction frame to be removed when game starts
    game_frame.pack()#Show the Game frame
    score = 0 
    update_score()
    update_lives()
    generate_question()
    start_timer()
#Function to generate questions    
def generate_question():
    global operator, num1, num2
    operator = random.choice(['+', '-', '*'])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question_label.config(text=f"What is {num1} {operator} {num2}?")
    answer_entry.delete(0, tk.END)
    answer_entry.focus()
#Function to check answer
def check_answer():
    global operator, num1, num2, score,lives
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
        lives-=1
        lives_label.config(text=int(lives))
        update_lives()
        if lives==0:
                result_label.config(text="Game over you have no lives !")
                reset_game()
                return
    update_lives()
    update_score()
    generate_question()

#updating the score
def update_score():
    score_label.config(text=f"Score: {score}")
def update_lives(): #update the lives
        lives_label.config(text=f'Lives:{lives}')
        
#start timer
def start_timer():
    global timer_running
    timer_running = True
    update_timer()
#update timer
def update_timer():
    global time_left, timer_running
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")
        timer_running = False
        reset_game()
        save_score()
#file handling        
def save_score():
        
    with open("score.txt", "w") as file:
        file.write(f"Final Score: {score}\n")

# instructions frame and label
instructions_frame = tk.Frame(root)
instructions_text = tk.Label(instructions_frame, text="Good luck\n"
                                 "You will have 10 seconds to answer each question\n"
                                 "Two lives to play the Game\n"
                                 "The Game will ask you basic maths question")
instructions_text.pack(pady=10)
#Reset game
def reset_game():
        global score,lives,time_left
        score=0
        lives=2
        time_left=10
        update_score()
        update_lives()
        result_label.config(text="")
        generate_question()
        start_timer()
        

# home screen frame
home_frame = tk.Frame(root)
home_frame.pack(pady=30)

# start button
start_button = tk.Button(home_frame, text='Start', width=20, command=show_instructions)
start_button.pack(padx=50, side=tk.LEFT)

# exit button
exit_button = tk.Button(home_frame, text='Exit', width=20, command=exit)
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
#lives label
lives_label=tk.Label(game_frame,text=f'Lives: {lives}')
lives_label.pack(pady=10)
#submit button
submit_button = tk.Button(game_frame, text="Submit", command=check_answer)
submit_button.pack(pady=10)
#result label
result_label = tk.Label(game_frame, text="")
result_label.pack(pady=10)
#score label
score_label = tk.Label(game_frame, text="Score: 0")
score_label.pack(pady=10)
#Timer label
timer_label = tk.Label(game_frame, text="Time Left: 10")
timer_label.pack(pady=10)
#Running the code
if __name__=="_main_":
        root=tk.Tk()
        app=CoolMathsGame(root)
        root.mainloop()

root.mainloop()



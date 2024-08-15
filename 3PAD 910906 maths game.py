
#910906
#3PAD
import random
from tkinter import*
import tkinter as tk
from tkinter import messagebox

#Adding Classes
class CoolMathsGame:
        def __init__(self,root):
                self.root=root
                self.root.title="Cool Maths Game"
                self.root.geometry="500x500"
                self.root.configure=bg="0352fc"
                self.show_menu_screen()
class CoolMathsGameQuestion:
        def _init(self):
                self.operation('+','-','*','/')
                self.question=""
                self.answer="None"



#Main screen
root=Tk()
root.title("Cool Maths Game")
root.geometry('300x300')
root.configure(bg="#0352fc")

#Adding image to my code
bg_canvas = Canvas(root, width=500, height=500)
bg_canvas.pack(fill="both", expand = True)
image_path=tk.PhotoImage(file=r"C:\Users\karti\OneDrive - Lynfield College\futuristic-threshold-with-reflections-on-wall-and-floor-free-video.png")
bg_canvas.create_image(500, 500, image=image_path)
#Question handling
lives = 2
score = 0
answer = None
question = None
operations = ["+", "-", "*"]
input_var = tk.StringVar()

def generate_question():
        global answer, question
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        operation = random.choice(operations)
        question = f"{num1}{operation} {num2}"
        answer = eval(question)
        print(answer)
        question_label.config(text=question)

def submit():
        global score, lives

        if lives == 0:
                messagebox.showerror(message="You are out of lives.")
                return

        try:
                if int(input_var.get()) == answer:
                       score += 1
                       score_Label.config(text=str(score))
                       generate_question()
                else:
                        messagebox.showinfo(message="Wrong")
                        lives -= 1
                        lives_label.config(text=str(lives))
                        generate_question()
        except Exception as e:
                messagebox.showerror(message=e)
#Game screen
title_label=tk.Label(text="Welcome to Cool Maths Game",font=('Arial,10'),bg='White',borderwidth=20)
title_label.place(relx=0.5, anchor="c", y=20)
start_button=tk.Button(text="Start",command=generate_question)
start_button.place(relx=0.5, anchor="c", y=60)
instruction_label=tk.Label(text="Solve the Maths questions:",font=('Arial,10'),bg="White",borderwidth=10)
instruction_label.place(relx=0.5, anchor="c", y=100)
question_label=tk.Label(text="2+2",font=('Arial,10'),bg='white',borderwidth=20)
question_label.place(relx=0.5, anchor="c", y=150)
answer_entry=tk.Entry(font=('Arial',10),textvariable=input_var)
answer_entry.place(relx=0.5, anchor="c", y=200)
submit_button=tk.Button(text="Submit", command=submit)
submit_button.place(relx=0.5, anchor="c", y=250)
tryAgain_button=tk.Button(text="TryAgain",font=('Arial,10'),command=generate_question)
tryAgain_button.place(relx=0.5, anchor="c", y=300)
score_Label=tk.Label(text="score=0",font=('Arial',20),bg="White",borderwidth=10)
score_Label.place(relx=0.5, anchor="c", y=350)
exit_label=tk.Button(text="Exit",font=('Arial',10),command=exit)
exit_label.place(x=0, anchor="nw", y=0)
lives_label=tk.Label(text=F"Lives:{lives}",font=('Arial',12),bg="White",borderwidth=10)
lives_label.place(relx=0.5, anchor="c", y=400)

#Running the code
if __name__=="_main_":
        root=tk.Tk()
        app=CoolMathsGame(root)
        root.mainloop()


generate_question()                          
root.mainloop()

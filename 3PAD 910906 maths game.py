#910906
#3PAD
import random
from tkinter import*
import tkinter as tk
from tkinter import messagebox
import os
import time 

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

#intalising the window
root=Tk()
root.title("Cool Maths Game")
root.geometry('500x500')
root.configure(bg="#0352fc")
#Second window
screen=Tk()
screen.title("Register screen")
screen.geometry('500x500')
screen.configure(bg="Green")
        
#Adding image to my code
bg_canvas = Canvas(root, width=500, height=500)
bg_canvas.pack(fill="both", expand = True)
image_path=tk.PhotoImage(file=r"C:\Users\karti\OneDrive - Lynfield College\3PAD program\futuristic-threshold-with-reflections-on-wall-and-floor-free-video.png")
bg_canvas.create_image(500, 500, image=image_path)
#Question handling
lives = 2
score = 0
timer=10
answer = None
question = None
operations = ["+", "-", "*"]
input_var = tk.StringVar()

def generate_question():
        global answer, question
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
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
#Labels and buttons 
title_label=tk.Label(root,text="Welcome to Cool Maths Game",font=('Arial,10'),bg='White',borderwidth=20)
title_label.place(relx=0.5, anchor="c", y=20)
start_button=tk.Button(root,text="Start",command=generate_question)
start_button.place(relx=0.5, anchor="c", y=60)
instruction_label=tk.Label(root,text="Solve the Maths questions:",font=('Arial,10'),bg="White",borderwidth=10)
instruction_label.place(relx=0.5, anchor="c", y=100)
question_label=tk.Label(root,text="2+2",font=('Arial,10'),bg='white',borderwidth=20)
question_label.place(relx=0.5, anchor="c", y=150)
answer_entry=tk.Entry(font=('Arial',10),textvariable=input_var)
answer_entry.place(relx=0.5, anchor="c", y=200)
submit_button=tk.Button(root,text="Submit", command=submit)
submit_button.place(relx=0.5, anchor="c", y=250)
tryAgain_button=tk.Button(root,text="TryAgain",font=('Arial,10'),command=generate_question)
tryAgain_button.place(relx=0.5, anchor="c", y=300)
score_Label=tk.Label(root,text="score=0",font=('Arial',20),bg="White",borderwidth=10)
score_Label.place(relx=0.5, anchor="c", y=350)
exit_label=tk.Button(root,text="Exit",font=('Arial',10),command=exit)
exit_label.place(x=0, anchor="nw", y=0)
lives_label=tk.Label(root,text=F"Lives:{lives}",font=('Arial',12),bg="White",borderwidth=10)
lives_label.place(relx=0.5, anchor="c", y=400)
timer_label=tk.Label(root,text="Timeleft=10seconds",font=('Arial',10),bg='white')
timer_label.place(relx=0.5,anchor="c",y=450)

#File handling
def save_student_info():
    first_name=first_name.get()
    last_name=last_name.get()
    student_id=student_id.get()
    user_score=user_score.get()
    student_id=input('Enter Student ID')
    first_name=input('Enter  first name')
    last_name=input('Enter your last name')
    user_score=input('Enter your final score')
    file.write(f"{desktop.initid},{name},{score}/n")
    print('User,Student data saved sucessfully')
    file=open('User.txt',"w")
    file.write('Firstname:',firstname_info)
    file.write('lastname:',lastname_info)
    file.write('studentid:',studentid_info)
    file.write('userscore:',userscore_info)
    file.close()
    print("user",Firstname_info,'has been registered successfully')
firstname=StringVar()
lastname=StringVar()
userscore=IntVar()
studentid=IntVar()
firstname_entry=Entry(screen, textvariable=firstname,width='30')
lastname_entry=Entry(screen, textvariable=lastname,width='30')
studentid_entry=Entry(screen, textvariable=studentid,width='30')
userscore_entry=Entry(screen, textvariable=userscore,width='30')
registered_button=tk.Button(screen, text="registerd",font=('Arial',10),bg="White",borderwidth=20)
registered_button.place(relx=0.5, anchor="c", y=300)
firstname_label=tk.Label(screen,text="Firstname",font=('Arial',10),bg="White")
lastname_label=tk.Label(screen,text="Lastname",font=('Arial',10),bg="White")
studentid_label=tk.Label(screen,text="Studentid",font=('Arial',10),bg="White")
userscore_label=tk.Label(screen,text="Userscore",font=('Arial',10),bg='White')
firstname_label.place(relx=0.5,anchor="e",y=100)
lastname_label.place(relx=0.5,anchor="e",y=150)
studentid_label.place(relx=0.5,anchor="e",y=200)
userscore_label.place(relx=0.5,anchor="e",y=250)
#entries
firstname_entry.place(relx=0.5,anchor="w",y=100)
lastname_entry.place(relx=0.5,anchor="w",y=150)
studentid_entry.place(x=0.5,anchor="w",y=200)
userscore_entry.place(x=0.5,anchor="w",y=250)


#Running the code
if __name__=="_main_":
        root=tk.Tk()
        app=CoolMathsGame(root)
        root.mainloop()

screen.mainloop()
generate_question()                          
root.mainloop()




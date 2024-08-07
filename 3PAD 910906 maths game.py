#910906
#3PAD
import random
from tkinter import*
import tkinter as tk
#creating a window
root=Tk()
root.title("Cool Maths Game")
root.geometry('500x500')
root.configure(bg="#0352fc")
#Adding image to my code
bg_canvas = Canvas(root, width=500, height=500)
bg_canvas.pack(fill="both", expand = True)
image_path=tk.PhotoImage(file=r"C:\Users\karti\OneDrive - Lynfield College\futuristic-threshold-with-reflections-on-wall-and-floor-free-video.png")
bg_canvas.create_image(500, 500, image=image_path)
#Welcome banner to My game
title_label=Label(root,text="Welcome to Cool Maths Game",font=('Arial,10'),bg='white',borderwidth=20)
title_label.place(relx=0.5, y=10)
#Start Game button
start=Button(root,text="Start")
start.place(relx=0.10, y=20, anchor="c")
#Input answer button
solving=Entry(root)
solving.place(relx=0.15,y=30)
#Submitting Button
submit=Button(root,text="Submit")
submit.place(relx=0.5,y=40)
#Try again button
TryAgain_label=Label(root,text="TryAgain",font=('Arial,10'),borderwidth=20)
TryAgain_label.place(relx=0.5,y=20)
#instruction for the Game
instruction_label=Label(root,text="Solve the Maths questions:",font=('Arial,10'),bg="White",borderwidth=10)
instruction_label.place(relx=0.5,y=50)
#Scoring for the Game
scoreLabel=Label(text="0/100",font=('Arial',20),bg="White",borderwidth=10)
scoreLabel.place(relx=0.5,y=60)
#Function to generate question
def generate_Maths_question():
        global num1,num2
num1=random.randint(0,10)
num2=random.randit(0,10)
question_label=('What is {num1}+{num2}')
question_entry.delete(0,Tk(end)
answer_label.config(text="")
generate_Maths_question()
root.mainloop()

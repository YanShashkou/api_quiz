import tkinter as tk
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.title("Quiz")
        self.score_label = tk.Label(text=f"score:{self.quiz.score}",bg=THEME_COLOR,fg='white', font=("Arial"))
        self.canvas = tk.Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(150,125,width=250,text='some question',font=("Arial",20,"italic"),fill='black')
        self.right_image=tk.PhotoImage(file='images/true.png')
        self.right_button = tk.Button(image=self.right_image,highlightthickness=0,command=self.true_click)
        self.wrong_image=tk.PhotoImage(file='images/false.png')
        self.wrong_button = tk.Button(image=self.wrong_image,highlightthickness=0,command=self.false_click)
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        self.wrong_button.grid(row=2, column=0)
        self.right_button.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.right_button.config(state='normal')
            self.wrong_button.config(state='normal')
        else:
            self.canvas.itemconfig(self.question_text,text='The end ')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_click(self):
        self.give_feedback(self.quiz.check_answer('True'))
    def false_click(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self,is_right):
        if is_right:
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score:{self.quiz.score}')

        if not is_right:
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
            self.canvas.config(bg='red')
            self.score_label.config(text=f'Score:{self.quiz.score}')
        self.window.after(1000,self.get_question)
from tkinter import *
import time
import random


# Button commands
def check_speed():
    entered_text = [i for i in text.get().split(" ")]
    words_guessed = 0
    for i in range(len(entered_text)):
        if entered_text[i] == words[i]:
            words_guessed += 1

    t1 = time.time()
    time_passed = t1-t0
    words_per_minute = (words_guessed / time_passed) * 60
    accuracy = (words_guessed / len(words)) * 100

    sentence.config(text=f'You write {int(words_per_minute)} words per minute!\nTime spent: {int(time_passed)} seconds!\nAccuracy: {accuracy}% ')
    text.config(state='disabled')
    button.config(text='Start', command=start)

def start():
    global t0
    global words

    with open('words.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    words = [random.choice(lines) for _ in range(20)]
    t0 = time.time()

    sentence.config(text=words)
    button.config(text='Submit', command=check_speed)
    text.config(state='normal')
    text.delete(0, END)


# Tkinter setup
window = Tk()
window.title('Speed Typing Test')
window.minsize(width=550, height=350)
window.maxsize(width=550, height=350)

title = Label(text="Typing Speed Test", font=('default', 30)).pack( pady=40)

sentence = Message(text="", width=500, anchor='center', font=('defualt',12), justify='center')
sentence.pack(pady=20)

text = Entry(width=500,font=('default', 15), state='disabled')
text.pack(pady=15)

button = Button(text='Start',width=12, command=start)
button.pack()


window.mainloop()
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0
music = False


def set():
    global t
    rem = sd.askstring('Время напоминания', 'Введите время напоминания')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t = dt.timestamp()
            print(t)
            text = sd.askstring('Текст напоминания', 'Введите текст напоминания')
            lab.config(text=f'Напоминание установлено на {hour:02}:{minute:02}: {text}')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}')

def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            print(now)
            play_snd()
            t = 0
    window.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    lab.config(text='Установить новое напоминание')

window = Tk()
window.title('Напоминание')
lab = Label(text='Установите напоминание', font=('Arial, 14'))
lab.pack(pady=10)
set_but = Button(text='Установить напоминание', command=set)
set_but.pack()
stop_but = Button(text='Остановить музыку', command=stop_music)
stop_but.pack(pady=10)

check()

window.mainloop()

from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None
music = False


def set():
    global t
    rem = sd.askstring('Время напоминания', 'Введите время в формате ЧЧ:ММ (24-часовой формат)')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            if hour in range(0, 24) and minute in range(0, 59):
                now = datetime.datetime.now()
                dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                t = dt.timestamp()
                text = sd.askstring('Текст напоминания', 'Введите текст напоминания')
                lab.config(text=f'Напоминание установлено на {hour:02}:{minute:02}: {text}')
            else:
                mb.showerror('Ошибка', 'Ошибка ввода времени')
                set()
        except ValueError:
            mb.showerror('Ошибка', 'Неверный формат времени')
            set()


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
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

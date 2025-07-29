from cProfile import label
from tkinter import *
from tkinter import ttk
from  tkinter import messagebox as mb
import  requests
from PIL import Image, ImageTk
from io import BytesIO

from bottle import response


def get_dog_img():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as e:
        mb.showerror('Ошибка', f'Возникла ошибка при запросе к API {e}')
        return None


def show_img():
    img_url = get_dog_img()
    if img_url:
        try:
            response = requests.get(img_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            new_window = Toplevel(window)
            new_window.title('Случайный пёсик')
            label = ttk.Label(new_window, image=img)
            label.pack()
            label.img = img
        except Exception as e:
            mb.showerror('Ошибка', f'Возникла ошибка при загрузке изображения {e}')
    progress.stop()

def prog():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, show_img)


window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

lab = ttk.Label()
lab.pack(pady=10)

but = ttk.Button(text='Загрузить изображение', command=prog)
but.pack(pady=10)

progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(pady=10)

width_lab = ttk.Label(text='Ширина: ')
width_lab.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

height_lab = ttk.Label(text='Высота: ')
height_lab.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))


window.mainloop()

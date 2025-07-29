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
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            lab.config(image=img)
            lab.img = img
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

window.mainloop()

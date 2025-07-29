from tkinter import *
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
        return data('message')
    except Exception as e:
        mb.showerror('Ошибка', f'Возникла ошибка при загрузке изображения {e}')
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
            mb.showerror('Ошибка', f'Возникла ошибка при запросе к API {e}')





window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

lab = Label()
lab.pack(pady=10)

but = Button(text='Загрузить изображения', command=show_img)
but.pack(pady=10)

window.mainloop()

from tkinter import *
import  requests
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

lab = Label()
lab.pack(pady=10)

but = Button(text='Загрузить изображения', command=show_img)
but.pack(pady=10)

window.mainloop()

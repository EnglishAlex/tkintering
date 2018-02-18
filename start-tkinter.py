from tkinter import *

from PIL import Image, ImageTk
class Window(Frame):
        def __init__(self, master = None):
                Frame.__init__(self, master)
                self.master = master
                self.init_window()

        def init_window(self):
                self.master.title("GUI")
                self.pack(fill=BOTH, expand=1)
                quitButton = Button(self, text="Quit", command=self.client_exit)
                quitButton.place(x=50,y=50)

                menu = Menu(self.master)
                self.master.config(menu=menu)
                file = Menu(menu)
                file.add_command(label='Save', command=self.client_exit)
                file.add_command(label='Open', command=self.client_exit)
                file.add_command(label='Close', command=self.client_exit)
                menu.add_cascade(label='File', menu=file)

                edit = Menu(menu)
                edit.add_command(label='Show Image', command=self.showImage)
                edit.add_command(label='Show Text', command=self.showText)
                menu.add_cascade(label='Edit', menu=edit)
                

        def client_exit(self):
                exit()
                
        def showImage(self):
                image = Image.open('moon1.png')
                render = ImageTk.PhotoImage(image)

                img = Label(self, image=render)
                img.image = render
                img.place(x=10,y=10)
                

        def showText(self):
                text = Label(self, text = 'Hey There')
                text.pack()
                
                
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()

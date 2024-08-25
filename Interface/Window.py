from tkinter import *


class Window:

    def __init__(self):
        self.root = Tk()
        self.root.title('Window')
        self.root.geometry('400x300')
        

    

    def add_label(self, text, x, y):
        self.label = Label(self.root, text=text)
        self.label.place(x=x, y=y)

    def add_button(self, text, x, y, command):
        self.button = Button(self.root, text=text, command=command)
        self.button.place(x=x, y=y)

    def add_entry(self):
        self.entry = Entry(self.root)
        self.entry.pack()

    def get_entry(self):
        return self.entry.get()
    
    def main_loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    window = Window()
    window.add_label('Hello, World!', 500, 100)
    window.add_button('Click me!', 10, 15,  lambda: window.add_label(window.get_entry()))
    window.add_entry()
    window.main_loop()
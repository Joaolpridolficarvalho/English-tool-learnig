from pathlib import Path
from tkinter import Tk, Entry, Button, PhotoImage, Label, Frame
from tkscrolledframe import ScrolledFrame
from Controller.Adapter import Adapter

class Home:
    def __init__(self):
        self.response_entry = None
        self.add_word_entry = None
        self.root = Tk()
        self.adapter = Adapter()
        self.setup_ui()
        self.show_words()
        self.root.mainloop()

    def __relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documentos\English\English-tool-learnig\Interface\assets")
        return ASSETS_PATH / Path(path)

    def add_word(self):
        word = self.get_add_word()
        self.adapter.process_request(word)
        self.add_word_entry.delete(0, 'end')
        self.show_words()

    def __create_response_entry(self):
        response = Entry(self.root, width=40, bg="white", fg='black')
        response.place(x=600, y=97)
        response.bind("<FocusIn>", self.__set_cursor)
        response.bind("<Return>", lambda event: print(self.get_response()))
        response.bind("<Tab>", self.__focus_next_widget)
        return response

    def show_words(self):
        words = self.adapter.return_list()
        for word in words:
            Label(self.inner_frame, text=word['word'], bg="#2784F2", fg=self.label_fill_color, font=(self.font_name, self.font_size)).pack()
    def get_response(self):
        return self.response_entry.get()

    def get_add_word(self):
        return self.add_word_entry.get()

    def __create_add_word_entry(self):
        add_word = Entry(self.root, width=35, bg="white", fg='black')
        add_word.place(x=1209, y=112)
        add_word.bind("<FocusIn>", self.__set_cursor)
        add_word.bind("<Return>", lambda event: self.add_word())
        add_word.bind("<Tab>", self.__focus_next_widget)
        return add_word

    def __create_response_button(self):
        self.response_entry_image = PhotoImage(file=self.__relative_to_assets("button_Response.png"))
        response_button = Button(image=self.response_entry_image, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        response_button.place(x=621.0, y=163.0, width=198.0, height=48.0)
        return response_button

    def __create_add_button(self):
        self.add_image = PhotoImage(file=self.__relative_to_assets("button_Add.png"))
        button_add = Button(image=self.add_image, borderwidth=0, highlightthickness=0, command=lambda: self.add_word(), relief="flat")
        button_add.place(x=1218.0, y=183.0, width=198.0, height=48.0)
        return button_add

    def __create_config_button(self):
        self.config_image = PhotoImage(file=self.__relative_to_assets("button_Config.png"))
        button_config = Button(image=self.config_image, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
        button_config.place(x=1350.0, y=15.0, width=48.0, height=48.0)
        return button_config

    def __set_cursor(self, event):
        event.widget.config(insertbackground='black')

    def __focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def setup_ui(self):
        self.root.geometry("1440x1024")
        self.root.configure(bg="#2784F2")
        self.root.resizable(True, True)
        self.font_name = "Inter"
        self.font_size = 16 * -1
        self.label_fill_color = "#FFFFFF"

        Label(self.root, text="Digite sua resposta ", bg="#2784F2", fg=self.label_fill_color, font=(self.font_name, self.font_size)).place(x=621.0, y=50.0)
        Label(self.root, text="Digite uma palavra ", bg="#2784F2", fg=self.label_fill_color, font=(self.font_name, self.font_size)).place(x=1250.0, y=65.0)
        Label(self.root, text="Palavras ", bg="#2784F2", fg=self.label_fill_color, font=(self.font_name, self.font_size)).place(x=1289.0, y=250.0)

        self.scrolled_frame = ScrolledFrame(self.root)
        self.scrolled_frame.tk_setPalette(background="#2784F2")
        self.scrolled_frame.place(x=1192.0, y=271.0, width=217.0, height=694.0)
        self.scrolled_frame.bind_arrow_keys(self.root)
        self.scrolled_frame.bind_scroll_wheel(self.root)
        self.scrolled_frame.configure(bg="#2784F2")

        self.inner_frame = self.scrolled_frame.display_widget(Frame, bg="#2784F2")

        self.response_button = self.__create_response_button()
        self.button_add = self.__create_add_button()
        self.button_config = self.__create_config_button()

        self.response_entry = self.__create_response_entry()
        self.add_word_entry = self.__create_add_word_entry()

if __name__ == "__main__":
    app = Home()
from pathlib import Path
from threading import Thread
from tkinter import Tk, Entry, Button, PhotoImage, Label, Frame
from tkscrolledframe import ScrolledFrame
from Controller.Adapter import Adapter
from Controller.Timer import timer


class Home:
    def __init__(self):
        self.response_entry = None
        self.add_word_entry = None
        self.random_word_label = None
        self.random_word_refresh_seconds = 5
        self.root = Tk()
        self.adapter = Adapter()
        self.setup_ui()
        self.show_words()
        self.__start_random_word_refresh_loop()
        self.root.mainloop()

    def __relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path.joinpath(OUTPUT_PATH, Path("assets"))
        return ASSETS_PATH / Path(path)

    def add_word(self):
        word = self.get_add_word()
        self.adapter.process_request(word)
        self.add_word_entry.delete(0, "end")
        self.show_words()
        self.__refresh_random_word_label()

    def __create_response_entry(self):
        response = Entry(self.root, width=40, bg="white", fg="black")
        response.place(x=600, y=97)
        response.bind("<FocusIn>", self.__set_cursor)
        response.bind("<Return>", lambda event: print(self.get_response()))
        response.bind("<Tab>", self.__focus_next_widget)
        return response

    def show_words(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        words = self.adapter.return_list()

        for word in words:
            text = word.get("word", str(word))
            Label(
                self.inner_frame,
                text=text,
                bg="#2784F2",
                fg=self.label_fill_color,
                font=(self.font_name, self.font_size),
            ).pack()

    def __get_random_word_text(self):
        shuffled_data = self.adapter.shuffle_dict()
        if not shuffled_data:
            return "Nenhuma palavra disponível"

        word_item, question_item = shuffled_data

        word_text = ""
        if isinstance(word_item, dict):
            word_text = word_item.get("word", "")
        elif word_item is not None:
            word_text = str(word_item)

        question_text = ""
        if isinstance(question_item, dict):
            question_text = question_item.get("text", "")
        elif question_item is not None:
            question_text = str(question_item)

        if question_text and word_text:
            return f"{question_text} {word_text}"
        if word_text:
            return word_text
        if question_text:
            return question_text
        return "Nenhuma palavra disponível"

    def __refresh_random_word_label(self):
        if self.random_word_label is not None:
            self.root.after(0, lambda: self.random_word_label.config(text=self.__get_random_word_text()))

    @timer()
    def __refresh_random_word_label_loop(self):
        self.__refresh_random_word_label()

    def __start_random_word_refresh_loop(self):
        self.__refresh_random_word_label()
        Thread(target=self.__refresh_random_word_label_loop, daemon=True).start()

    def get_response(self):
        return self.response_entry.get()

    def get_add_word(self):
        return self.add_word_entry.get()

    def __create_add_word_entry(self):
        add_word = Entry(self.root, width=35, bg="white", fg="black")
        add_word.place(x=1209, y=112)
        add_word.bind("<FocusIn>", self.__set_cursor)
        add_word.bind("<Return>", lambda event: self.add_word())
        add_word.bind("<Tab>", self.__focus_next_widget)
        return add_word

   
    def __create_button(self, x, y, width, height, command, image_path):
        image = PhotoImage(file=self.__relative_to_assets(image_path))
        setattr(self, f"_button_image_{id(image)}", image)  # Store image reference
        button = Button(
            image=image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat",
        )
        button.place(x=x, y=y, width=width, height=height)
        return button

    def __set_cursor(self, event):
        event.widget.config(insertbackground="black")

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

        Label(
            self.root,
            text="Digite sua resposta ",
            bg="#2784F2",
            fg=self.label_fill_color,
            font=(self.font_name, self.font_size),
        ).place(x=621.0, y=50.0)
        Label(
            self.root,
            text="Digite uma palavra ",
            bg="#2784F2",
            fg=self.label_fill_color,
            font=(self.font_name, self.font_size),
        ).place(x=1250.0, y=65.0)
        Label(
            self.root,
            text="Palavras ",
            bg="#2784F2",
            fg=self.label_fill_color,
            font=(self.font_name, self.font_size),
        ).place(x=1289.0, y=250.0)

        self.scrolled_frame = ScrolledFrame(self.root)
        self.scrolled_frame.tk_setPalette(background="#2784F2")
        self.scrolled_frame.place(x=1192.0, y=271.0, width=217.0, height=694.0)
        self.scrolled_frame.bind_arrow_keys(self.root)
        self.scrolled_frame.bind_scroll_wheel(self.root)
        self.scrolled_frame.configure(bg="#2784F2")

        self.inner_frame = self.scrolled_frame.display_widget(Frame, bg="#2784F2")
        self.random_word_label = Label(
            self.root,
            text=self.__get_random_word_text(),
            bg="#2784F2",
            fg=self.label_fill_color,
            font=(self.font_name, self.font_size),
        )
        self.random_word_label.place(x=610.0, y=80.0)

        self.response_button = self.__create_button(
            x=621.0,
            y=163.0,
            width=198.0,
            height=48.0,
            command=lambda: print("button_1 clicked"),
            image_path="button_Response.png",
        )
        self.button_add = self.__create_button(
            1218.0, 183.0, 198.0, 48.0, lambda: self.add_word(), "button_Add.png"
        )
        # self.button_config = self.__create_button(1350.0, 15.0, 48.0, 48.0, lambda: print("button_3 clicked"), "button_Config.png")

        self.response_entry = self.__create_response_entry()
        self.add_word_entry = self.__create_add_word_entry()


if __name__ == "__main__":
    app = Home()

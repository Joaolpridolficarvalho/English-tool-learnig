from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, Frame
from tkscrolledframe import ScrolledFrame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documentos\English\English-tool-learnig\Interface\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_item(text):
    global item_count
    Label(inner_frame, text=f"{text}", font=(font_name, 14), bg="#2784F2", fg="white").grid(row=item_count, column=0, sticky="w")
    item_count += 1

window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#2784F2")
window.resizable(True, True)
font_name = "Inter"
font_size = 16 * -1
label_fill_color = "#FFFFFF"

canvas = Canvas(window, bg = "#2784F2", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

scrolled_frame = ScrolledFrame(window, bg="#2784F2")
scrolled_frame.place(x=1192.0, y=271.0, width=217.0, height=694.0)
scrolled_frame.bind_arrow_keys(window)
scrolled_frame.bind_scroll_wheel(window)
scrolled_frame.configure(bg="#2784F2")

inner_frame = scrolled_frame.display_widget(Frame, bg="#2784F2")

# Modificar a cor das barras de rolagem
#scrolled_frame.vertical_scrollbar.config(bg="#2784F2")
#.horizontal_scrollbar.config(bg="#2784F2")

item_count = 0

for i in range(5):
    add_item(f"Item {i+1}")

response_image = PhotoImage(file=relative_to_assets("button_Response.png"))
response_button = Button(image=response_image, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"),
                  relief="flat")
response_button.place(x=621.0, y=163.0, width=198.0, height=48.0)

add_image = PhotoImage(file=relative_to_assets("button_Add.png"))
button_add = Button(image=add_image, borderwidth=0, highlightthickness=0, command=lambda: add_item("Novo item"),
                  relief="flat")
button_add.place(x=1218.0, y=183.0, width=198.0, height=48.0)

canvas.create_text(1289.0, 250.0, anchor="nw", text="Palavras ", fill=label_fill_color, font=(font_name, font_size))
canvas.create_text(621.0, 50.0, anchor="nw", text="Digite sua resposta ", fill=label_fill_color, font=(font_name, font_size))
canvas.create_text(1250.0, 50.0, anchor="nw", text="Digite uma palavra ", fill=label_fill_color, font=(font_name, font_size))

response = Entry(window, width=40)
response.place(x=600, y=97)

add_word = Entry(window, width=35)
add_word.place(x=1209, y=97)

window.resizable(False, False)
window.mainloop()

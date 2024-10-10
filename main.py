import os
import sys
from PIL import Image, ImageTk
import tkinter as tk
from config import configure_app
from styles import StyleManager
from functions import *



app = tk.Tk()
configure_app(app)
style = StyleManager()

# determina o diretório base
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


# criação dos caminhos completos para as imagens usadas na app
trash_icon_path = os.path.join(base_path, "img", "trash-icon.png")
copy_icon_path = os.path.join(base_path, "img", "copy-icon.png")


# carrega as imagens em objetos que o Tkinter pode usar como ícones
trash_icon = ImageTk.PhotoImage(Image.open(trash_icon_path))
copy_icon = ImageTk.PhotoImage(Image.open(copy_icon_path))



label_text = tk.Label(app, text="Indique um texto:", bg=style.bg_color, fg=style.fg_color, font=style.title_font)
label_text.pack(pady=style.padding_y)

entry_text = tk.Text(app, width=50, height=2)
style.apply_entry_style(entry_text)
entry_text.pack(pady=style.padding_y)
entry_text.bind("<KeyRelease>", lambda event: update_counts(entry_text, word_count_label, char_count_label))


# frame principal para as colunas
frame_main = tk.Frame(app, bg=style.bg_color)
frame_main.pack(pady=style.padding_y)


# frame para os tipos de case
frame_cases = tk.Frame(frame_main, bg=style.bg_color)
frame_cases.grid(row=0, column=0, padx=style.padding_x)

label_case = tk.Label(frame_cases, text="TIPOS DE CASE")
style.apply_label_style(label_case)
label_case.pack(pady=style.padding_y)

# defini-se o texto e as funções que os botões devolvem ao clicar neles
for case_name, func in [("camelCase", camel_case), ("snake_case", snake_case), ("PascalCase", pascal_case),
                        ("kebab-case", kebab_case), ("UPPER CASE", upper_case), ("lower case", lower_case),
                        ("AlTeRnAtE CaSe", alternate_case), ("Title Case", title_case)]:
    button = tk.Button(frame_cases, text=case_name, command=lambda f=func: show_result(f, entry_text, result_entry))
    style.apply_button_style(button)
    button.pack(pady=style.padding_y)

# frame para as funcionalidades extra
frame_extras = tk.Frame(frame_main, bg=style.bg_color)
frame_extras.grid(row=0, column=1, padx=style.padding_x)

label_extra = tk.Label(frame_extras, text="EXTRA")
style.apply_label_style(label_extra)
label_extra.pack(pady=style.padding_y)

# botões para as funcionalidades extra
for extra_name, func in [("Inverter Texto", reverse_text), ("Remover Espaços", remove_spaces)]:
    button = tk.Button(frame_extras, text=extra_name, command=lambda f=func: show_result(f, entry_text, result_entry))
    style.apply_button_style(button)
    button.pack(pady=style.padding_y)


label_stats = tk.Label(frame_extras, text="ESTATÍSTICAS")
style.apply_label_style(label_stats)
label_stats.pack(pady=style.padding_y)

word_count_label = tk.Label(frame_extras, text="Número de palavras: 0", bg=style.bg_color, fg=style.fg_color, font=style.label_font)
word_count_label.pack(pady=style.padding_y)

char_count_label = tk.Label(frame_extras, text="Número de caracteres: 0", bg=style.bg_color, fg=style.fg_color, font=style.label_font)
char_count_label.pack(pady=style.padding_y)

# Resultado
label_result = tk.Label(app, text="Resultado:", bg=style.bg_color, fg=style.fg_color, font=style.title_font)
label_result.pack(pady=style.padding_y)
result_entry = tk.Text(app, width=50, height=2)
style.apply_entry_style(result_entry)
result_entry.pack(pady=style.padding_y)
result_entry.config(state='disabled')

# frame dos botões limpar e copiar
frame_buttons = tk.Frame(app, bg=style.bg_color)
frame_buttons.pack(pady=style.padding_y)

# botões limpar e copiar
btn_clear = tk.Button(frame_buttons, text="Limpar", image=trash_icon, compound="left", command=lambda: clear_content(entry_text, result_entry))
style.apply_button_style(btn_clear)
btn_clear.config(width=80)
btn_clear.pack(side=tk.LEFT, padx=style.padding_x, pady=style.padding_y)

btn_copy = tk.Button(frame_buttons, text="Copiar", image=copy_icon, compound="left", command=lambda: copy_to_clipboard(app, result_entry))
style.apply_button_style(btn_copy)
btn_copy.config(width=80)
btn_copy.pack(side=tk.LEFT, padx=style.padding_x, pady=style.padding_y)

app.mainloop()


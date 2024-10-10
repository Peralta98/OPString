import tkinter as tk
from tkinter import messagebox

def camel_case(text):
    words = text.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def snake_case(text):
    return '_'.join(text.lower().split())

def pascal_case(text):
    return ''.join(word.capitalize() for word in text.split())

def kebab_case(text):
    return '-'.join(text.lower().split())

def upper_case(text):
    return text.upper()

def lower_case(text):
    return text.lower()

def alternate_case(text):
    return ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])

def title_case(text):
    return text.title()

def reverse_text(text):
    return text[::-1]

def remove_spaces(text):
    return text.replace(" ", "")

def update_counts(entry_text, word_count_label, char_count_label):
    text = entry_text.get("1.0", tk.END).strip()
    words_count = f"Número de palavras: {len(text.split())}"
    characters_count = f"Número de caracteres: {len(text)}\n(Sem espaços: {len(text.replace(' ', ''))})"
    word_count_label.config(text=words_count)
    char_count_label.config(text=characters_count)

def show_result(func, entry_text, result_entry):
    text = entry_text.get("1.0", tk.END).strip()
    if text:
        result = func(text)
        result_entry.config(state='normal')
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, result)
        result_entry.config(state='disabled')
    else:
        messagebox.showerror("Erro", "Por favor, insere um texto.")

def clear_content(entry_text, result_entry):
    entry_text.delete("1.0", tk.END)
    result_entry.config(state='normal')
    result_entry.delete("1.0", tk.END)
    result_entry.config(state='disabled')

def copy_to_clipboard(app, result_entry):
    app.clipboard_clear()
    result = result_entry.get("1.0", tk.END).strip()
    app.clipboard_append(result)
    messagebox.showinfo("Cópia", "O resultado foi copiado para a área de transferência.")

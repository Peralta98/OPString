class StyleManager:
    def __init__(self):
        # fontes e tamanhos
        self.title_font = ("Helvetica", 12, "bold")
        self.label_font = ("Helvetica", 10)
        self.button_font = ("Helvetica", 10)
        self.entry_font = ("Helvetica", 12)

        # esquema de cores da app
        self.bg_color = "#1c1c1c"
        self.fg_color = "white"  # texto principal
        self.entry_bg_color = "#333333"  # fundo da entrada de texto
        self.button_bg_color = "#333"
        self.hover_color = "#7600c9"
        self.button_active_bg_color = "#4d0680"
        self.label_bg_color = "#7600c9"  # cor roxa das labels
        self.label_fg_color = "#fcf7ff"  # cor do texto das labels

        # estilos dos botões
        self.button_style = {
            "bg": self.button_bg_color,
            "fg": self.fg_color,
            "font": self.button_font,
            "activebackground": self.button_active_bg_color,
            "relief": "flat", # retira o efeito default de border dos botões
            "padx": 20,
            "pady": 10,
            "width": 15
        }

        # estilos de entrada de texto
        self.entry_style = {
            "bg": self.entry_bg_color,
            "fg": self.fg_color,
            "insertbackground": self.fg_color,  # cor do ponto de inserção do input
            "font": self.entry_font,
            "relief": "flat"
        }

        # padding e espaçamento entre elementos
        self.padding_y = 5
        self.padding_x = 5

    # Aplicar estilo nos botões
    def apply_button_style(self, button):
        button.config(**self.button_style)
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        e.widget.config(bg=self.hover_color, cursor="hand2")

    def on_leave(self, e):
        e.widget.config(bg=self.button_style['bg'])

    def apply_label_style(self, label):
        label.config(bg=self.label_bg_color, fg=self.label_fg_color, font=self.title_font, padx="25px", pady="10px")

    # aplicar estilo de entrada de texto
    def apply_entry_style(self, entry):
        entry.config(**self.entry_style)

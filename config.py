import os
import sys


def configure_app(app):
    # Determina o diretório base
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    # Define o caminho do ícone
    icon_path = os.path.join(base_path, "favicon-op.ico")

    try:
        app.iconbitmap(icon_path)  # Define o ícone da aplicação
    except Exception as e:
        print(f"Erro ao definir o ícone: {e}")

    # Configuração da janela
    app.title("OPString")
    app.config(bg="#1c1c1c")  # cor de fundo da app

    screen_width = app.winfo_screenwidth()

    window_width = 750
    window_height = 768

    position_x = int((screen_width - window_width) / 2) # para obter a medida centralizada horizontalmente
    position_y = 100

    app.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    # app.geometry(750x800+pos_x+pos_y)

    # desabilita o redimensionamento (largura e altura) e o botão de maximizar
    app.resizable(False, False)
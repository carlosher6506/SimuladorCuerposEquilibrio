from tkinter import font
import tkinter as tk
from pages.Static_Balance import main

class PhysicsMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Física")
        self.root.geometry("1200x800")
        self.root.configure(bg="black")
        
        # Fuente personalizada
        self.custom_font = font.Font(family="Helvetica", size=16, weight="bold")
        
        # Crear la interfaz
        self.create_title()
        self.create_buttons()
        
    # Función para crear el título
    def create_title(self):
        title = tk.Label(self.root, text="Physics Simulator", font=("Helvetica", 24, "bold"), fg="#00ffcc", bg="black")
        title.pack(pady=20)
    
    # Función para crear los botones
    def create_buttons(self):
        # Botón "Jugar"
        jugar_button = tk.Button(self.root, text="Cuerpos en Equilibrio", font=self.custom_font, fg="white", bg="black", bd=0, highlightthickness=0, command=self.jugar)
        jugar_button.pack(pady=10)
        jugar_button.bind("<Enter>", lambda event, b=jugar_button: self.on_enter(event, b))
        jugar_button.bind("<Leave>", lambda event, b=jugar_button: self.on_leave(event, b))

        # Botón "Opciones"
        opciones_button = tk.Button(self.root, text="Opciones", font=self.custom_font, fg="white", bg="black", bd=0, highlightthickness=0, command=self.opciones)
        opciones_button.pack(pady=10)
        opciones_button.bind("<Enter>", lambda event, b=opciones_button: self.on_enter(event, b))
        opciones_button.bind("<Leave>", lambda event, b=opciones_button: self.on_leave(event, b))

        # Botón "Salir"
        salir_button = tk.Button(self.root, text="Salir", font=self.custom_font, fg="white", bg="black", bd=0, highlightthickness=0, command=self.salir)
        salir_button.pack(pady=10)
        salir_button.bind("<Enter>", lambda event, b=salir_button: self.on_enter(event, b))
        salir_button.bind("<Leave>", lambda event, b=salir_button: self.on_leave(event, b))

    # Método para el botón "Jugar"
    def jugar(self):
        self.root.withdraw()  # Oculta el menú principal
        main()  # Llama a la función principal del simulador

    # Método para el botón "Opciones"
    def opciones(self):
        options_window = tk.Toplevel(self.root)
        options_window.title("Opciones")
        options_window.geometry("400x300")
        options_window.configure(bg="gray")
        label = tk.Label(options_window, text="Configuración del simulador", font=("Helvetica", 14), bg="gray", fg="white")
        label.pack(pady=20)

    # Método para el botón "Salir"
    def salir(self):
        self.root.quit()  # Cierra la aplicación

    # Función de hover para los botones
    def on_enter(self, event, button):
        button.config(fg="#00ffcc")

    # Función para quitar el hover
    def on_leave(self, event, button):
        button.config(fg="white")
#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox
import os

class RemoteControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RCU Virtual")
        self.root.geometry("400x800")
        
        # Estado
        self.status_label = tk.Label(root, text="RCU Virtual - Listo", font=("Arial", 14))
        self.status_label.pack(pady=10)

        # Botones y comandos ADB
        buttons = [
            {"text": "Power", "command": "input keyevent 26"},
            {"text": "Vol +", "command": "input keyevent 24"},
            {"text": "Vol -", "command": "input keyevent 25"},
            {"text": "Back", "command": "input keyevent 4"},
            {"text": "Home", "command": "input keyevent 3"},
            {"text": "Menu", "command": "am start -a android.settings.SETTINGS"},
            {"text": "Arriba", "command": "input keyevent 19"},
            {"text": "Abajo", "command": "input keyevent 20"},
            {"text": "Izquierda", "command": "input keyevent 21"},
            {"text": "Derecha", "command": "input keyevent 22"},
            {"text": "OK", "command": "input keyevent 66"},
        ]

        # Crear botones
        for button in buttons:
            btn = tk.Button(root, text=button["text"], font=("Arial", 12), width=15, height=2,
                            command=lambda cmd=button["command"]: self.send_adb_command(cmd))
            btn.pack(pady=5)

    def send_adb_command(self, command):
        """
        Enviar comando ADB a la Set-Top Box.
        """
        try:
            os.system(f"adb shell {command}")
            self.status_label.config(text=f"Comando enviado: {command}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo enviar el comando.\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RemoteControlApp(root)
    root.mainloop()

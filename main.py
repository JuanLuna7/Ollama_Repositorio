import tkinter as tk
from app.ui import ChatApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
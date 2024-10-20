import tkinter as tk

class FirstWindow:
    def __init__(self, master):
        self.master = master
        master.title("First Window")
        master.geometry("300x200")
        self.button = tk.Button(master, text="Open Second Window", command=self.open_second_window)
        self.button.pack()

    def open_second_window(self):
        self.master.destroy()
        second_window = tk.Tk()
        SecondWindow(second_window)

class SecondWindow:
    def __init__(self, master):
        self.master = master
        master.title("Second Window")
        master.geometry("300x200")
        self.label = tk.Label(master, text="Welcome to the second window!")
        self.label.pack()
        master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FirstWindow(root)
    root.mainloop()

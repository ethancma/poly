import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.geometry('500x500')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.size_changer=tk.Button(self)
        self.size_changer["text"] = "Size changer"
        self.size_changer["command"] = self.change_size
        self.size_changer.pack(side="top")
        
        self.a = tk.Label(self,text="s")
        self.a.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        self.a.config(text="hello")

    def change_size(self):
        self.master.geometry('150x150')

root = tk.Tk()
app = Application(master=root)
app.mainloop()

import random
from tkinter import *
from tkinter import messagebox

class GUI:

    def __init__(self, window):
        self.window=window
        window.title("Random Group Generator for the Golf Buddies (By Rob Smith)")
        window.geometry("1000x800")

        self.lbl1=Label(window, text="Who is Playing:", font = ("Arial Bold", 20))
        self.lbl1.place(x=20, y=25)

        self.chk_state1=BooleanVar()
        self.chk_state1.set(False)
        self.chk_state2=BooleanVar()
        self.chk_state2.set(False)
        self.chk_state3=BooleanVar()
        self.chk_state3.set(False)
        self.chk_state4=BooleanVar()
        self.chk_state4.set(False)
        self.chk_state5=BooleanVar()
        self.chk_state5.set(False)
        self.chk_state6=BooleanVar()
        self.chk_state6.set(False)
        self.chk_state7=BooleanVar()
        self.chk_state7.set(False)
        self.chk_state8=BooleanVar()
        self.chk_state8.set(False)
        self.chk1=Checkbutton(window, text="Butch", font=("Arial", 14), var=self.chk_state1)
        self.chk2=Checkbutton(window, text="Little Ron", font=("Arial", 14), var=self.chk_state2)
        self.chk3=Checkbutton(window, text="Faffer Yates", font=("Arial", 14), var=self.chk_state3)
        self.chk4=Checkbutton(window, text="El Gringo", font=("Arial", 14), var=self.chk_state4)
        self.chk5=Checkbutton(window, text="Riggers", font=("Arial", 14), var=self.chk_state5)
        self.chk6=Checkbutton(window, text="NR Man", font=("Arial", 14), var=self.chk_state6)
        self.chk7=Checkbutton(window, text="Judith Chalmers", font=("Arial", 14), var=self.chk_state7)
        self.chk8=Checkbutton(window, text="Speedy Gonzalez", font=("Arial", 14), var=self.chk_state8)
        self.chk1.place(x=20, y=75)
        self.chk2.place(x=20, y=125)
        self.chk3.place(x=20, y=175)
        self.chk4.place(x=20, y=225)
        self.chk5.place(x=250, y=75)
        self.chk6.place(x=250, y=125)
        self.chk7.place(x=250, y=175)
        self.chk8.place(x=250, y=225)

        self.lbl2=Label(window, text= "Is the booking for:", font=("Arial Bold", 20))
        self.lbl2.place(x=20, y=275)

        self.rbvar = IntVar(window, FALSE)
        self.rb1=Radiobutton(window, variable=self.rbvar, text="Pairs", value=1, font=("Arial", 14))
        self.rb2=Radiobutton(window, variable=self.rbvar, text="Trios", value=2, font=("Arial", 14))
        self.rb3=Radiobutton(window, variable=self.rbvar, text="Quads", value=3, font=("Arial", 14))
        self.rb4=Radiobutton(window, variable=self.rbvar, text="7 players (Groups are a 3, 2 & 2)", value=4, font=("Arial", 14))
        self.rb1.place(x=20, y=325)
        self.rb2.place(x=20, y=360)
        self.rb3.place(x=20, y=395)
        self.rb4.place(x=20, y=430)

        self.btn=Button(window, text="Press to Generate Groups", font=("Arial Bold", 16), command=self.generate_groups)
        self.btn.place(x=20, y=500)

    def generate_groups(self):
        self.name_list=[]
        if self.chk_state1.get()==TRUE:
            self.name_list.append("Butch")
        if self.chk_state2.get()==TRUE:
            self.name_list.append("Little Ron")
        if self.chk_state3.get()==TRUE:
            self.name_list.append("Faffer Yates")
        if self.chk_state4.get()==TRUE:
            self.name_list.append("El Gringo")
        if self.chk_state5.get()==TRUE:
            self.name_list.append("Riggers")
        if self.chk_state6.get()==TRUE:
            self.name_list.append("NR Man")
        if self.chk_state7.get()==TRUE:
            self.name_list.append("Judith Chalmers")
        if self.chk_state8.get()==TRUE:
            self.name_list.append("Speedy Gonzalez")
        #print(name_list)

        match self.rbvar.get():
            case 1:
                if len(self.name_list) < 2:
                    messagebox.showinfo("Pairs", "Not enough players selected")
                else:
                    pass
            case 2:
                if len(self.name_list) < 3:
                    messagebox.showinfo("Trios", "Not enough players selected")
            case 3:
                if len(self.name_list) < 4:
                    messagebox.showinfo("Quads", "Not enough players selected")
            case 4:
                if len(self.name_list) != 7:
                    messagebox.showinfo("Seven", "Incorrect number of players selected")
            case _:
                pass

def generate_name_pairs(names) -> list:
    pairs = []
    random.shuffle(names)
    for i in range(0, len(names), 2):
        if i + 1 < len(names):
            pairs.append((names[i], names[i + 1]))
    return pairs

def main():
    window=Tk()
    main_gui = GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()

from tkinter import *

def generate_groups():
    name_list=[]
    if chk_state1.get()==TRUE:
        name_list.append("Butch")
    if chk_state2.get()==TRUE:
        name_list.append("Little Ron")
    if chk_state3.get()==TRUE:
        name_list.append("Faffer Yates")
    if chk_state4.get()==TRUE:
        name_list.append("El Gringo")
    if chk_state5.get()==TRUE:
        name_list.append("Riggers")
    if chk_state6.get()==TRUE:
        name_list.append("NR Man")
    if chk_state7.get()==TRUE:
        name_list.append("Judith Chalmers")
    if chk_state8.get()==TRUE:
        name_list.append("Speedy Gonzalez")
    print(name_list)

    match rbvar.get():
        case 1:
            print("Pairs")
        case 2:
            print("Trios")
        case 3:
            print("Quads")
        case 4:
            print("Sevens")
    
window=Tk()
window.title("Random Group Generator for the Golf Buddies (By Rob Smith)")

window.geometry("1000x800")

Label(window, text="Who is Playing:", font = ("Arial Bold", 20)).place(x=20, y=25)

chk_state1=BooleanVar()
chk_state1.set(False)
chk_state2=BooleanVar()
chk_state2.set(False)
chk_state3=BooleanVar()
chk_state3.set(False)
chk_state4=BooleanVar()
chk_state4.set(False)
chk_state5=BooleanVar()
chk_state5.set(False)
chk_state6=BooleanVar()
chk_state6.set(False)
chk_state7=BooleanVar()
chk_state7.set(False)
chk_state8=BooleanVar()
chk_state8.set(False)
chk1=Checkbutton(window, text="Butch", font=("Arial", 14), var=chk_state1)
chk2=Checkbutton(window, text="Little Ron", font=("Arial", 14), var=chk_state2)
chk3=Checkbutton(window, text="Faffer Yates", font=("Arial", 14), var=chk_state3)
chk4=Checkbutton(window, text="El Gringo", font=("Arial", 14), var=chk_state4)
chk5=Checkbutton(window, text="Riggers", font=("Arial", 14), var=chk_state5)
chk6=Checkbutton(window, text="NR Man", font=("Arial", 14), var=chk_state6)
chk7=Checkbutton(window, text="Judith Chalmers", font=("Arial", 14), var=chk_state7)
chk8=Checkbutton(window, text="Speedy Gonzalez", font=("Arial", 14), var=chk_state8)
chk1.place(x=20, y=75)
chk2.place(x=20, y=125)
chk3.place(x=20, y=175)
chk4.place(x=20, y=225)
chk5.place(x=250, y=75)
chk6.place(x=250, y=125)
chk7.place(x=250, y=175)
chk8.place(x=250, y=225)

Label(window, text= "Is the booking for:", font=("Arial Bold", 20)).place(x=20, y=275)
rbvar = IntVar(window, FALSE)
rb1=Radiobutton(window, variable=rbvar, text="Pairs", value=1, font=("Arial", 14))
rb2=Radiobutton(window, variable=rbvar, text="Trios", value=2, font=("Arial", 14))
rb3=Radiobutton(window, variable=rbvar, text="Quads", value=3, font=("Arial", 14))
rb4=Radiobutton(window, variable=rbvar, text="7 players (Groups are a 3, 2 & 2)", value=4, font=("Arial", 14))
rb1.place(x=20, y=325)
rb2.place(x=20, y=360)
rb3.place(x=20, y=395)
rb4.place(x=20, y=430)

btn=Button(window, text="Press to Generate Groups", font=("Arial Bold", 16), command=generate_groups)
btn.place(x=20, y=500)

window.mainloop()

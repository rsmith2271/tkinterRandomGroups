import random
from tkinter import * # type: ignore
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class Login_Window:
    def __init__(self, master) -> None:
        self.master = master
        master.title("Login")
        master.geometry("450x400")

        self.lbl1=Label(master, text="HGC Login Details:", font = ("Arial Bold", 14))
        self.lbl1.place(x=145, y=25)
        self.lbl2=Label(master, text="User Number: ", font = ("Arial Bold", 14))
        self.lbl2.place(x=50, y=100)
        self.user=Entry(master, width=4, font = ("Arial Bold", 14))
        self.user.place(x=200, y=100)
        self.lbl3=Label(master, text="PIN: ", font = ("Arial Bold", 14))
        self.lbl3.place(x=50, y=150)
        bullet = "\u2022" #specifies bullet character
        self.pin=Entry(master, width=4, show=bullet, font = ("Arial Bold", 14))
        self.pin.place(x=200, y=150)

        self.button=Button(master, text="Login", font = ("Arial Bold", 20), command=self.loginHGC)
        self.button.place(x=170, y=200)
    
    def loginHGC(self) -> None:
        # Define the URL for the login form and the payload
        self.user_input: str=self.user.get()
        self.user_pin: str=self.pin.get()
        
        login_url = 'https://www.heskethgolfclub.co.uk/login.php'  # login URL 
        payload: dict[str, str] = {'memberid': self.user_input, 'pin': self.user_pin} 

        self.handicap_list=[]
        # Start a session 
        with requests.Session() as session: 
            # Send a POST request to log in 
            response = session.post(login_url, data=payload) 
        
            # Check if login was successful (actually a 200 response from the server, not a proper login check)
            cdh_list=[1003133540, 1007201368, 1012673068, 1004511710, 1013191007, 1000396043, 1012782936, 1001078566]
            for item in cdh_list:
                if response.ok: 
                    #print("Login successful!")

                    # You can now use `session` to access pages that require login 
                    self.protected_url = f"https://www.heskethgolfclub.co.uk/whshcaprecord.php?playerid= {item}"  # Replace with a protected URL 
                    self.protected_response = session.get(self.protected_url) 
            
                    if self.protected_response.ok:
                        pass
                        #print(f"Accessed protected page!") 
                        # Do something with the protected page content 
                        #print(protected_response.text) 
                    else: 
                        print("Failed to access protected page.") 
                else: 
                    print("Login failed.")

                soup = BeautifulSoup(self.protected_response.content, 'html.parser')

                # Find all the text elements (e.g., paragraphs, headings, etc.) you want to scrape
                text_elements = soup.find_all(['p'])

                # Extract the text from each element and concatenate them into a single string
                scraped_text = ' '.join(element.get_text() for element in text_elements)
                            
                hcap_index = scraped_text.find("Current Handicap Index: ")
                self.current_handicap=scraped_text[hcap_index+24:hcap_index+28]
                self.handicap_list.append(self.current_handicap)

            self.open_second_window()

    def open_second_window(self) -> None:
        self.master.destroy()
        window = Tk()
        GUI(window, self.handicap_list)

class GUI:

    def __init__(self, window, handicap_list) -> None:
        self.window=window
        window.title("Random Group Generator")
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
        self.chk1=Checkbutton(window, text=f"Rob Smith (H.I.: {handicap_list[0]})", font=("Arial", 14), var=self.chk_state1) # type: ignore
        self.chk2=Checkbutton(window, text=f"Rob Smallman (H.I.: {handicap_list[1]})", font=("Arial", 14), var=self.chk_state2) # type: ignore
        self.chk3=Checkbutton(window, text=f"Richard (H.I.: {handicap_list[2]})", font=("Arial", 14), var=self.chk_state3) # type: ignore
        self.chk4=Checkbutton(window, text=f"Brian (H.I.: {handicap_list[3]})", font=("Arial", 14), var=self.chk_state4) # type: ignore
        self.chk5=Checkbutton(window, text=f"Ian (H.I.: {handicap_list[4]})", font=("Arial", 14), var=self.chk_state5) # type: ignore
        self.chk6=Checkbutton(window, text=f"Steve (H.I.: {handicap_list[5]})", font=("Arial", 14), var=self.chk_state6) # type: ignore
        self.chk7=Checkbutton(window, text=f"Kev (H.I.: {handicap_list[6]})", font=("Arial", 14), var=self.chk_state7) # type: ignore
        self.chk8=Checkbutton(window, text=f"Si (H.I.: {handicap_list[7]})", font=("Arial", 14), var=self.chk_state8) # type: ignore
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
        self.rb2=Radiobutton(window, variable=self.rbvar, text="Threes", value=2, font=("Arial", 14))
        self.rb3=Radiobutton(window, variable=self.rbvar, text="Fours", value=3, font=("Arial", 14))
        self.rb4=Radiobutton(window, variable=self.rbvar, text="7 players (Groups are a 3, 2 & 2)", value=4, font=("Arial", 14))
        self.rb1.place(x=20, y=325)
        self.rb2.place(x=20, y=360)
        self.rb3.place(x=20, y=395)
        self.rb4.place(x=20, y=430)

        self.btn=Button(window, text="Press to Generate Groups", font=("Arial Bold", 16), command=self.generate_groups)
        self.btn.place(x=20, y=500)

    def generate_groups(self) -> None:
        if self.rbvar.get() ==0:
            messagebox.showinfo("There's an issue!", "No group selected!")
        if self.chk_state1.get()==FALSE & self.chk_state2.get()==FALSE & self.chk_state3.get()==FALSE & self.chk_state4.get()==FALSE & self.chk_state5.get()==FALSE & self.chk_state6.get()==FALSE & self.chk_state7.get()==FALSE & self.chk_state8.get()==FALSE:
            messagebox.showinfo("There's an issue!", "No names selected!")

        self.name_list=[]
        if self.chk_state1.get()==TRUE:
            self.name_list.append("Rob Smith")
        if self.chk_state2.get()==TRUE:
            self.name_list.append("Rob Smallman")
        if self.chk_state3.get()==TRUE:
            self.name_list.append("Richard")
        if self.chk_state4.get()==TRUE:
            self.name_list.append("Brian")
        if self.chk_state5.get()==TRUE:
            self.name_list.append("Ian")
        if self.chk_state6.get()==TRUE:
            self.name_list.append("Steve")
        if self.chk_state7.get()==TRUE:
            self.name_list.append("Kev")
        if self.chk_state8.get()==TRUE:
            self.name_list.append("Si")
        #print(name_list)

        match self.rbvar.get():
            case 1:
                if len(self.name_list) < 2:
                    messagebox.showinfo("Pairs", "Not enough players selected")
                else:
                    self.lbl3=Label(self.window, text= "The groups are:", font=("Arial Bold", 16))
                    self.lbl3.place(x=20, y=575)

                    random.shuffle(self.name_list)
                    self.pairs = [self.name_list[i:i + 2] for i in range(0, len(self.name_list) - 1, 2)]

                    i=1
                    ycoord=625
                    for pair in self.pairs:
                        self.lbl4=Label(self.window, text=f"{i}. {pair[0]} & {pair[1]}", font=("Arial Bold", 14))
                        self.lbl4.place(x=20, y=ycoord)
                        i += 1
                        ycoord+= 25
                    if len(self.name_list) % 2 != 0:
                        self.lbl5=Label(self.window, text=f"{i}. {self.name_list[-1]} is on his own", font=("Arial Bold", 14))
                        self.lbl5.place(x=20, y=ycoord)
            
            case 2:
                if len(self.name_list) < 3:
                    messagebox.showinfo("Threes", "Not enough players selected")
                else:
                    self.lbl6=Label(self.window, text= "The groups are:", font=("Arial Bold", 16))
                    self.lbl6.place(x=20, y=575)

                    random.shuffle(self.name_list)
                    self.threes = [self.name_list[i:i + 3] for i in range(0, len(self.name_list) - 2, 3)]
                    
                    i=1
                    ycoord=625
                    for three in self.threes:
                        self.lbl7=Label(self.window, text=f"{i}. {three[0]} & {three[1]} & {three[2]}", font=("Arial Bold", 14))
                        self.lbl7.place(x=20, y=ycoord)
                        i += 1
                        ycoord+= 25
                    div3: int = len(self.name_list)%3
                    match div3:
                        case 1:
                            self.lbl8=Label(self.window, text=f"{i}. {self.name_list[-1]} is on his own", font=("Arial Bold", 14))
                            self.lbl8.place(x=20, y=ycoord)
                        case 2:
                            self.lbl9=Label(self.window, text=f"{i}. {self.name_list[-1]} & {self.name_list[-2]}", font=("Arial Bold", 14))
                            self.lbl9.place(x=20, y=ycoord)
                        case _:
                            pass

            case 3:
                if len(self.name_list) < 4:
                    messagebox.showinfo("Fours", "Not enough players selected")
                else:
                    self.lbl10=Label(self.window, text= "The groupss are:", font=("Arial Bold", 16))
                    self.lbl10.place(x=20, y=575)

                    random.shuffle(self.name_list)
                    self.fours = [self.name_list[i:i + 4] for i in range(0, len(self.name_list) - 3, 4)]
                    
                    i=1
                    ycoord=625
                    for four in self.fours:
                        self.lbl11=Label(self.window, text=f"{i}. {four[0]} & {four[1]} & {four[2]} & {four[3]}", font=("Arial Bold", 14))
                        self.lbl11.place(x=20, y=ycoord)
                        i += 1
                        ycoord+= 25
                    div4: int = len(self.name_list)%4
                    match div4:
                        case 1:
                            self.lbl12=Label(self.window, text=f"{i}. {self.name_list[-1]} is on his own", font=("Arial Bold", 14))
                            self.lbl12.place(x=20, y=ycoord)
                        case 2:
                            self.lbl13=Label(self.window, text=f"{i}. {self.name_list[-1]} & {self.name_list[-2]}", font=("Arial Bold", 14))
                            self.lbl13.place(x=20, y=ycoord)
                        case 3:
                            self.lbl14=Label(self.window, text=f"{i}. {self.name_list[-1]} & {self.name_list[-2]} & {self.name_list[-3]}", font=("Arial Bold", 14))
                            self.lbl14.place(x=20, y=ycoord)
                        case _:
                            pass

            case 4:
                if len(self.name_list) != 7:
                    messagebox.showinfo("Seven", "Incorrect number of players selected")
                else:
                    self.lbl15=Label(self.window, text= "The groups are:", font=("Arial Bold", 16))
                    self.lbl15.place(x=20, y=575)

                    random.shuffle(self.name_list)
                    self.pairs = [self.name_list[i:i + 2] for i in range(0, len(self.name_list) - 1, 2)]

                    self.lbl16=Label(self.window, text=f"1. {self.pairs[0][0]} & {self.pairs[0][1]} & {self.name_list[-1]}", font=("Arial Bold", 14))
                    self.lbl17=Label(self.window, text=f"2. {self.pairs[1][0]} & {self.pairs[1][1]}", font=("Arial Bold", 14))
                    self.lbl18=Label(self.window, text=f"2. {self.pairs[2][0]} & {self.pairs[2][1]}", font=("Arial Bold", 14))
                    self.lbl16.place(x=20, y=625)
                    self.lbl17.place(x=20, y=650)
                    self.lbl18.place(x=20, y=675)
            case _:
                pass

def main() -> None:
    master=Tk()
    main_gui = Login_Window(master)
    master.mainloop()

if __name__ == "__main__":
    main()

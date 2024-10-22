import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        '''
        self.title("Main Window")
        self.geometry("300x200")

        # Variable to be used in the second window
        self.shared_variable = tk.StringVar(value="Hello from Main Window")

        # Button to open the second window
        self.open_window_button = tk.Button(self, text="Open Second Window", command=self.open_second_window)
        self.open_window_button.pack(pady=20)

    def open_second_window(self):
        SecondWindow(self)
        '''
        self.title("Login")
        self.geometry("450x400")

        self.lbl1=Label(self, text="HGC Login Details:", font = ("Arial Bold", 14))
        self.lbl1.place(x=145, y=25)
        self.lbl2=Label(self, text="User Number: ", font = ("Arial Bold", 14))
        self.lbl2.place(x=50, y=100)
        self.user=Entry(self, width=4, font = ("Arial Bold", 14))
        self.user.place(x=200, y=100)
        self.lbl3=Label(self, text="PIN: ", font = ("Arial Bold", 14))
        self.lbl3.place(x=50, y=150)
        bullet = "\u2022" #specifies bullet character
        self.pin=Entry(self, width=4, show=bullet, font = ("Arial Bold", 14))
        self.pin.place(x=200, y=150)

        self.button=Button(self, text="Login", font = ("Arial Bold", 20), command=self.loginHGC)
        self.button.place(x=170, y=200)

    def loginHGC(self):
        # Define the URL for the login form and the payload
        self.user_input=self.user.get()
        self.user_pin=self.pin.get()
        
        login_url = 'https://www.heskethgolfclub.co.uk/login.php'  # login URL 
        payload = {'memberid': self.user_input, 'pin': self.user_pin} 
                
        # Start a session 
        with requests.Session() as session: 
            # Send a POST request to log in 
            response = session.post(login_url, data=payload) 
        
            # Check if login was successful (actually a 200 response from the server, not a proper login check)
            if response.ok: 
                #print("Login successful!")

                # You can now use `session` to access pages that require login 
                self.protected_url = 'https://www.heskethgolfclub.co.uk/whshcaprecord.php?playerid=1003133540'  # Replace with a protected URL 
                protected_response = session.get(self.protected_url) 
         
                if protected_response.ok:
                    pass
                    #print(f"Accessed protected page!") 
                    # Do something with the protected page content 
                    #print(protected_response.text) 
                else: 
                    print("Failed to access protected page.") 
            else: 
                print("Login failed.")

            soup = BeautifulSoup(protected_response.content, 'html.parser')

            # Find all the text elements (e.g., paragraphs, headings, etc.) you want to scrape
            text_elements = soup.find_all(['p'])

            # Extract the text from each element and concatenate them into a single string
            scraped_text = ' '.join(element.get_text() for element in text_elements)
                        
            hcap_index = scraped_text.find("Current Handicap Index: ")
            self.current_handicap1003133540=scraped_text[hcap_index+24:hcap_index+28]
            print(f"Current Index: {self.current_handicap1003133540}")
            self.open_second_window()

            # Variable to be used in the second window
            #self.shared_variable = tk.StringVar(value="Hello from Main Window")
    
    def open_second_window(self):
        SecondWindow(self)

class SecondWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title(f"Second Window {master.current_handicap1003133540}")
        self.geometry("300x300")

        # Access the shared variable from the main window
        #self.label = Label(self, textvariable=master.current_handicap1003133540)
        self.lbl1=Label(self, text=f"Handicap Index: {master.current_handicap1003133540}", font = ("Arial Bold", 14))
        self.lbl1.pack(pady=20)

        # Entry to update the shared variable
        #self.entry = tk.Entry(self, textvariable=master.current_handicap1003133540)
        #self.entry.pack(pady=20)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

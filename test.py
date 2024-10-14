from tkinter import *  

def printResults():
    print(var1.get())

a=Tk()  
a.geometry("400x400")  
a.title("test")    
  
Label(a, text="Select your country of birth: ").pack(anchor='w')

var1 = StringVar(a, "USA")  # Create a variable for strings, and initialize the variable
Radiobutton(a, text="USA", variable=var1, value="USA", command=printResults).pack(anchor='w')
Radiobutton(a, text="France", variable=var1, value="France", command=printResults).pack(anchor='w')
Radiobutton(a, text="Germany", variable=var1, value="Germany", command=printResults).pack(anchor='w')
Radiobutton(a, text="China", variable=var1, value="China", command=printResults).pack(anchor='w')

a.mainloop()  
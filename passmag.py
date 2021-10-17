from tkinter import *
from tkinter import messagebox
from random import *
import json

def GenerateRandomPassword():

         DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
         LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z'] 
         UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']
         SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

         generate_password = []
         rand_password = ""
         generate_password += choices(DIGITS, k = 2)
         generate_password += choices(LOCASE_CHARACTERS, k = 4)
         generate_password += choices(UPCASE_CHARACTERS, k = 3)
         generate_password += choices(SYMBOLS, k = 3)
         
         shuffle(generate_password)
         
         rand_password = "".join(generate_password)

         Password_Entry.delete(0, END) 
         Password_Entry.insert(0, string=rand_password)
         Status_Label['text'] = "Strong Password Generated"
         Status_Label['fg'] = "Green"
         Status_Label.grid(row= 5, column=1)
         Status_Label.after(2000, hide_label, Status_Label)
         


def hide_label(label_object):
    label_object.grid_forget()

def FetchWebsiteData():
        if(Website_Entry.get() == ""):
              Status_Label['text'] = "Please enter the Website Name"
              Status_Label['fg'] = "Red"
              Status_Label.grid(row= 5, column=1)
              Status_Label.after(2000, hide_label, Status_Label)
        else:
            website = Website_Entry.get()
            try:
                with open("pass.json", "r") as pass_file:
                    data_file = json.load(pass_file)
            except FileNotFoundError:
                messagebox.showerror(title=website, message="Data File not Found")
            else:
                if website in data_file:
                    messagebox.showinfo(title=website, 
                                message=f"E-Mail: {data_file[website]['email']}\nPassword: {data_file[website]['password']}")
                else:
                    messagebox.showerror(title=website, message=f"No details for {website} exists.")
    
def save_data():
    hide_label(Status_Label)
    if(Website_Entry.get() == "" or User_Entry.get() == "" or Password_Entry.get() == ""):
              Status_Label['text'] = "Something Went Wrong!"
              Status_Label['fg'] = "Red"
              Status_Label.grid(row= 5, column=1)
              Status_Label.after(2000, hide_label, Status_Label)
              return 0
    
    manage_data = {
           Website_Entry.get(): {
               "email": User_Entry.get(),
                "password": Password_Entry.get()
           }
    }
    
    try:

        with open("pass.json", "r") as pass_file:
             pass_data = json.load(pass_file)

    except FileNotFoundError:
         
         with open("pass.json", "w") as pass_file:
             json.dump(manage_data, pass_file, indent= 6)
    
    else:
        pass_data.update(manage_data)

        with open("pass.json", "w") as pass_file:
             json.dump(pass_data, pass_file, indent= 6)
    finally:
        Status_Label['text'] = "Your Credentials has been saved"
        Status_Label['fg'] = "Green"
        Status_Label.grid(row= 5, column=1)
        Status_Label.after(2000, hide_label, Status_Label)
        Website_Entry.delete(0, END)
        User_Entry.delete(0, END)
        Password_Entry.delete(0, END)



Window = Tk()
Window.title("Password Manager")
Window.resizable(width=False, height= False) 

Window.config(padx=70, pady=30)


#Create Icon
pass_icon = Canvas(Window,height=200, width=200)
pass_icon_img = PhotoImage(file="Webp.net-resizeimage.png")
pass_icon.create_image(100, 100, image=pass_icon_img)
pass_icon.grid(row=0, column=1)

Website_label = Label(Window,text="Website:")
Website_label.grid(row= 1, column=0)
User_label = Label(Window,text="E-Mail:")
User_label.grid(row = 2, column=0)
Password_label = Label(Window,text="Passowrd:")
Password_label.grid(row= 3, column=0)
Status_Label = Label(Window,text="Your Credentials has been saved", fg="Green", font=("Courier", 8, "bold") )
Status_Label.grid(row= 5, column=1)
Status_Label.grid_forget()


Website_Entry = Entry(Window,width=35)
Website_Entry.grid(row = 1, column=1)
User_Entry = Entry(Window,width=35)
User_Entry.grid(row = 2, column=1)
Password_Entry = Entry(Window,width=35)
Password_Entry.grid(row= 3, column=1)

Search_data_button = Button(Window,text="Search", width=15 ,command=FetchWebsiteData)
Search_data_button.grid(row=1, column=2)

Generate_password_button = Button(Window,text="Generate Password", command=GenerateRandomPassword)
Generate_password_button.grid(row=3, column=2)

add_button = Button(Window, text="Add", width=30, command = save_data)
add_button.grid(row=4, column=1)


Window.mainloop()

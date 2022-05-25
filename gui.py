from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if(email == 'flipkart@gmail.com' and password =='1234'):
        messagebox.showinfo('yayyy' , 'Login Successful')
    else :
        messagebox.showerror('error' , 'login Failed')

root = Tk()
root.title('Login Form')
root.iconbitmap('myicon.ico')
#root.minsize(400,400)
#root.maxsize(450,450)
root.geometry('350x500')
root.configure(background = '#0096DC')
img = Image.open('fkart.png')
img = img.resize((70,70))
img = ImageTk.PhotoImage(img)
img_label = Label(root,image = img)
img_label.pack(pady=(10,10))

text_label = Label(root,text = 'Flipkart', fg='white', bg= '#0096DC')
text_label.pack()
text_label.config(font = ('verdana',24))

email_label = Label(root, text = 'Enter Email' , fg = 'white' ,bg ='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font = ('verdana',12))
email_input = Entry(root , width= 50)
email_input.pack(ipady= 4 , pady=(1,15))

password_label = Label(root, text = 'Enter Password' , fg = 'white' ,bg ='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font = ('verdana',12))
password_input = Entry(root , width= 50)
password_input.pack(ipady= 4 , pady=(1,15))

login_btn = Button(root, width= 20 , height= 3, text = 'Login Here' , bg = 'white' , fg = 'black' , command= handle_login)
login_btn.pack(pady = (10,20))
root.mainloop()
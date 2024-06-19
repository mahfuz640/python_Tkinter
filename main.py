import tkinter

window = tkinter.Tk()
window.title("Login Form")
window.geometry('640x440')
# window.configure(bg='#333333')

label =tkinter.Label (window,text ="Login")
label.pack(row=0,colom=0)

window.mainloop()


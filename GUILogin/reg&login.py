from tkinter import *
import os

def register_user():
    username_info = username.get()
    password_info = password.get()
    handle = open("gui_creds.txt", "a")
    handle.write(username_info)
    handle.write(" ")
    handle.write(password_info)
    handle.write("\n")
    handle.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text="Registration Success", fg="green", font=("Calibri", 11)).pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()

def login_verify():
    get_data = open("gui_creds.txt", "r").readlines()
    users_data = []
    for user in get_data:
        users_data.append(user.split())

    total_user = len(users_data)
    increment = 0
    login_success = 0
    username1 = username_verify.get()
    password1 = password_verify.get()
    while increment < total_user:
        usernames = users_data[increment][0]
        passwords = users_data[increment][1]
        if username1 == usernames and password1 == passwords:
            login_success = 1

        increment += 1

    if login_success == 1:
        Label(screen2, text="Successful Login", fg="green", font=("Calibri", 10)).pack()
    else:
        Label(screen2, text="Failed Login", fg="green", font=("Calibri", 10)).pack()
        print(username1, password1)
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter your details below to login").pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0",
          bg="grey",
          width="300",
          height="2",
          font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    screen.mainloop()


main_screen()

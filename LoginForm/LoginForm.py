from login import Login

Login.username = "Admin"
Login.password = "testingTheWater56"


def log_form_resub():
    resub = input("Would you like to try again? (y/n): ")
    if resub == "y":
        log_form(Login.username, Login.password)


def log_form(uname, password):
    uname = input("Please Enter Username: ")
    password = input("Please Enter Password: ")
    if uname == Login.username:
        if password == Login.password:
            print("Login Successful!")
        else:
            log_form_resub()


log_form(Login.username, Login.password)

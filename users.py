class User:
    name = ""
    email = ""
    password = ""
    mobile = ""
    address = ""
    login_status = False;

    def __init__(self, name, email, password, mobile, address):
        self.name = name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.address = address

    def login(self):
        input_email = input("Enter Email: ")
        input_password = input("Enter Password: ")

        if input_email == self.email and input_password == self.password:
            self.login_status= True
            print("Login successful")
            self.user_profile()
        else:
            self.login_status = False
            print("Login failed")

    def logout(self):
        self.login_status = False
        print("Logged out")

    def is_logged_out(self):
        if self.login_status:
            return True
        else:
            return False

    def user_profile(self):
        if self.login_status:
            print("User Name: " + self.name + "\n" + "Email: " + self.email + "\n" + "Mobile: " + self.mobile + "\n" + "Address: " + self.address)
        else:
            print("User not logged in. profile not show.")


user1 = User("Sanat Mondal", "cse.sanat@gmail.com", "12345", "01712995265", "Dhaka, Mirpur-2")

user1.login()

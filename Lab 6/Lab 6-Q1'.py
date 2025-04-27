class Password_manager:
    def __init__(self):
        self.old_passwords = []


    def get_password(self):
        if self.old_passwords:  
            return self.old_passwords[-1] 
        
        else:
            return None 

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password changed successfully.")
        else:
            print("This password has been used before")

    def is_correct(self, password):
        return password == self.get_password()


pm = Password_manager()

while True:
    print("\n1. Set Password")
    print("2. Get Current Password")
    print("3. Check Password")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        new_password = input("Enter new password: ")
        pm.set_password(new_password)

    elif choice == "2":
        print("Current Password:", pm.get_password())

    elif choice == "3":
        password = input("Enter password to check: ")
        if pm.is_correct(password):
            print("Password is correct.")
        else:
            print("Incorrect password.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

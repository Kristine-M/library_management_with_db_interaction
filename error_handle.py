def valid_input(): #this function makes sure the user enters a valid input
    while True:
        try:
            user_input = int(input("\nWhich task do you want to do? "))
            if user_input not in range(1, 4):
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a valid number between 1 and 3")
            
        finally: 
            print("----------------------------------------------")
            
def main_menu_valid_input(): #this function makes sure the user enters a valid input
    while True:
        try:
            user_input = int(input("\nWhich task do you want to do? "))
            if user_input not in range(1, 6):
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a valid number between 1 and 5")
            
        finally: 
            print("----------------------------------------------")
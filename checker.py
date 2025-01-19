def load_password_list(file_path):
    """
    Load a list of passwords from a text file.
    """
    try:
        # Specify the encoding to handle different character encodings
        with open(file_path, 'r', encoding='latin-1') as file:
            passwords = file.read().splitlines()
        return passwords
    except FileNotFoundError:
        print("Password list file not found!")
        return []
    except UnicodeDecodeError as e:
        print(f"Error decoding file: {e}")
        return []

def crack_password(target_password, password_list):
    """
    Attempt to find the target password in the provided list.
    """
    attempts = 0 #create attempt counter
    for password in password_list:
        attempts += 1 #increment attempt counter
        print(f"Trying password: {password}")  # Debugging output
        if password == target_password:
            print(f"Number of attempts: {attempts}") 
            return password
           
      
    return None

def main():
    # Set the target password (for demonstration purposes)
    target_password = input("Enter the password you want to check: ")

    # Path to the password list file
    password_list_file = "rockyou.txt"

    # Load the password list
    password_list = load_password_list(password_list_file)

    if not password_list:
        print("No passwords to test.")
        return

    # Attempt to crack the password
    result = crack_password(target_password, password_list)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found in the list.")

if __name__ == "__main__":
    main()

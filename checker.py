def load_password_list(file_paths):
    """
    Load a list of passwords from multiple text files.
    """
    passwords = []
    for file_path in file_paths:
        try:
            # Specify the encoding to handle different character encodings
            with open(file_path, 'r', encoding='latin-1') as file:
                passwords.extend(file.read().splitlines())
        except FileNotFoundError:
            print(f"Password list file {file_path} not found!")
        except UnicodeDecodeError as e:
            print(f"Error decoding file {file_path}: {e}")
    return passwords

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

    # Paths to the password list files
    password_list_files = ["rockyou1.txt", "rockyou2.txt"]

    # Load the password list
    password_list = load_password_list(password_list_files)

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

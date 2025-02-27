import hashlib
import os

# File to store the passwords and site names
FILENAME = 'passwords.txt'

# Function to hash the password
def hash_password(password):
    """ Hash a password for storing"""

    return(hashlib.sha256(password.encode()).hexdigest())

# Function to save the password
def save_password(site, password):
    """ Save the site name and password"""
    hashed_password = hash_password(password)
    with open (FILENAME, "a") as file:
        file.write(f"{site} {hashed_password}\n")
    print(f"Password for {site} saved successfully")

# Function to get the password
def get_password(site):
    """Retrieve the password for the site"""
    if not os.path.exists(FILENAME):
        print("No password saved  yet")
        return
    with open(FILENAME, "r") as f:
        for line in f:
            stored_site, stored_password = line.strip().split(" ")
            if stored_site == site:
                return stored_password
    print(f"No password saved for {site}")
    return None

def site_exists(site):
    """Check if the site already exists in the file"""
    if not os.path.exists(FILENAME):
        return False
    with open(FILENAME, "r") as f:
        for line in f:
            stored_site, _ = line.strip().split(" ")
            if stored_site == site:
                return True
    return False

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass #Create the file if it does nt exist

def main():
    action = input("Enter 'save' to save a password or 'get' to retrieve a password:  ")

    if action == "save":
        site = input("Enter the site: ")
        if site_exists(site):
            print("site already exists")
            overwrite = input("Do you want to update the password? (yes/no):")
            if overwrite != "yes":
                print("Password not updated")
                return
        import string
        import random
        # Generate a random password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=10))
        print(f"Generated password: {password}")
        save_password(site, password)
    elif action == "get":
        site = input("Enter the site name: ")
        password = get_password(site)
        if password:
            print(f"Password for {site} is {password}")

    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
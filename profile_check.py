import os

def check_profile():
    username = os.getlogin()  # Get the current user's username
    current_dir = os.getcwd()  # Get the current working directory

    if current_dir.endswith(username):
        profile_path = os.path.join(current_dir, '.profile.txt')

        # Check if profile.txt exists
        if os.path.isfile(profile_path):
            with open(profile_path, 'r') as file:
                content = file.readlines()
                name, phone, email = [line.strip() for line in content]
                print(f"Name: {name}\nPhone: {phone}\nEmail: {email}")
                confirm = input("Is this information up to date? (yes/no): ")

                if confirm.lower() == 'yes':
                    print("Great! You can continue using the terminal.")
                else:
                    update_profile(profile_path)
        else:
            print("No profile.txt found. Creating a new one...")
            update_profile(profile_path)

    else:
        print(f"Creating new directory for {username}...")
        new_dir = os.path.join(os.path.expanduser('~'), username)
        os.makedirs(new_dir, exist_ok=True)
        profile_path = os.path.join(new_dir, '.profile.txt')
        update_profile(profile_path)

def update_profile(profile_path):
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")

    with open(profile_path, 'w') as file:
        file.write(f"{name}\n{phone}\n{email}\n")
    
    print("Profile updated! You can continue using the terminal.")

if __name__ == "__main__":
    check_profile()

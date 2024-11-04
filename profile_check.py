import os

home_dir = os.path.expanduser('~')

def getUsername():
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown_user'

def validate_input(prompt, expected_type):
    while True:
        user_input = input(prompt)
        if expected_type == 'str':
            return user_input.strip()
        elif expected_type == 'phone':
            if user_input.isdigit() and len(user_input) in [10, 11]:
                return user_input.strip()
            else:
                print("Please enter a valid phone number (10 or 11 digits).")
        elif expected_type == 'email':
            if "@" in user_input and "." in user_input:
                return user_input.strip()
            else:
                print("Please enter a valid email address.")

def check_profile():
    username = getUsername()
    print(f"Welcome, {username}!")

    if home_dir.endswith(username):
        profile_path = os.path.join(home_dir, ".profile.txt")

        if os.path.isfile(profile_path):
            with open(profile_path, 'r') as file:
                content = file.readlines()
                if len(content) < 3:
                    print("Profile file is incomplete. Please update your profile.")
                    update_profile(profile_path)
                    return
                
                name, phone, email = [line.strip() for line in content]
                print(f"Name: {name}\nPhone: {phone}\nEmail: {email}")
                confirm = input("Is this information up to date? (yes/no): ")

                if confirm.lower() == 'yes':
                    print("You can continue using the terminal.")
                else:
                    update_profile(profile_path)
        else:
            print("No profile.txt found. Creating a new one...")
            update_profile(profile_path)

    else:
        print(f"Creating new directory for {username}...")
        os.makedirs(home_dir, exist_ok=True)
        profile_path = os.path.join(home_dir, '.profile.txt')
        update_profile(profile_path)

def update_profile(profile_path):
    name = validate_input("Enter your name: ", 'str')
    phone = validate_input("Enter your phone number (10 or 11 digits): ", 'phone')
    email = validate_input("Enter your email: ", 'email')

    with open(profile_path, 'w') as file:
        file.write(f"{name}\n{phone}\n{email}\n")
    
    print("Profile updated! You can continue using the terminal.")

if __name__ == "__main__":
    check_profile()

# enter a password which contain at least 8 characters, a special character, a number and a character   
password = input("Enter your password: ")

special_characters_found = False
has_number = False
has_character = False
special_characters = ['@', '#', '$', '%', '&', '*', '!']

for char in password:
    if char in special_characters:
        special_characters_found = True
    elif char.isdigit():
        has_number = True
    elif char.isalpha():
        has_character = True

if len(password) < 8:
    print("Weak password")
elif special_characters_found and has_number and has_character:
    print("Strong password")
else:
    print("Moderate password")

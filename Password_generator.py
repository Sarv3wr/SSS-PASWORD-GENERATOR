import random
import string

def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_characters
        
    pwd = ""
    meets_criteria = False
    has_num = False
    has_special = False
    
    while not meets_criteria and len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_num = True
            
        elif new_char in special_characters:
            has_special = True
        
        meet_criteria = True
        if numbers:
            meets_criteria = False
        if special_characters:
            meets_criteria = meets_criteria and has_special
            
    return pwd

min_lenght = int(input("enter your minimum number of characters: "))
has_number = input("Do you want numbers? (y/n): ").lower() == "y"
has_special = input("Do you want  special characters? (y/n): ").lower() == "y"

pwd = generate_password(min_lenght, has_number, has_special)
print( "Your password is: ",pwd)
            

        
        
        
 